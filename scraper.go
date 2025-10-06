package main

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"net/url"
	"os"
	"strings"
	"sync"
	"time"
)

// PhoneBookLOCA v1.1 - OSINT Web Scraper
// Go scraper maintained by: 0xb0rn3 | oxbv1

// Result represents a single search result
type Result struct {
	Source      string   `json:"source"`
	URL         string   `json:"url"`
	Title       string   `json:"title,omitempty"`
	Snippet     string   `json:"snippet,omitempty"`
	Found       bool     `json:"found"`
	Error       string   `json:"error,omitempty"`
	ResponseTime float64 `json:"response_time"`
}

// OSINTResults holds all results from different sources
type OSINTResults struct {
	PhoneNumber string   `json:"phone_number"`
	Timestamp   string   `json:"timestamp"`
	Results     []Result `json:"results"`
	Summary     Summary  `json:"summary"`
}

// Summary provides quick insights
type Summary struct {
	TotalSources   int      `json:"total_sources"`
	FoundIn        int      `json:"found_in"`
	FailedSources  int      `json:"failed_sources"`
	Platforms      []string `json:"platforms_found"`
	PossibleEmails []string `json:"possible_emails"`
}

func main() {
	if len(os.Args) < 2 {
		fmt.Fprintln(os.Stderr, "Usage: scraper <phone_number>")
		os.Exit(1)
	}

	phoneNumber := os.Args[1]
	
	// Print progress to stderr so stdout is clean JSON
	fmt.Fprintf(os.Stderr, "[*] Starting OSINT web scraping for: %s\n", phoneNumber)
	fmt.Fprintf(os.Stderr, "[*] Using concurrent Go routines for maximum speed...\n\n")

	results := performOSINT(phoneNumber)

	// Output ONLY JSON to stdout
	jsonData, err := json.MarshalIndent(results, "", "  ")
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error marshaling JSON: %v\n", err)
		os.Exit(1)
	}

	fmt.Println(string(jsonData))
}

func performOSINT(phoneNumber string) OSINTResults {
	results := OSINTResults{
		PhoneNumber: phoneNumber,
		Timestamp:   time.Now().Format(time.RFC3339),
		Results:     []Result{},
	}

	// Define all sources to check
	sources := []struct {
		name string
		fn   func(string) Result
	}{
		{"Google", searchGoogle},
		{"Facebook", searchFacebook},
		{"LinkedIn", searchLinkedIn},
		{"Twitter", searchTwitter},
		{"Instagram", searchInstagram},
		{"TrueCaller", checkTrueCaller},
		{"Pastebin", searchPastebin},
		{"GitHub", searchGitHub},
	}

	// Use WaitGroup for concurrent execution
	var wg sync.WaitGroup
	resultsChan := make(chan Result, len(sources))

	// Launch all searches concurrently
	for _, source := range sources {
		wg.Add(1)
		go func(name string, searchFn func(string) Result) {
			defer wg.Done()
			result := searchFn(phoneNumber)
			resultsChan <- result
		}(source.name, source.fn)
	}

	// Wait for all goroutines to complete
	go func() {
		wg.Wait()
		close(resultsChan)
	}()

	// Collect results
	platforms := []string{}
	foundCount := 0
	failedCount := 0

	for result := range resultsChan {
		results.Results = append(results.Results, result)
		
		if result.Found {
			foundCount++
			platforms = append(platforms, result.Source)
		}
		if result.Error != "" {
			failedCount++
		}

		// Print progress to stderr (not stdout, so JSON stays clean)
		status := "✗"
		if result.Found {
			status = "✓"
		}
		fmt.Fprintf(os.Stderr, "[%s] %s (%.2fs)\n", status, result.Source, result.ResponseTime)
	}

	// Build summary
	results.Summary = Summary{
		TotalSources:  len(sources),
		FoundIn:       foundCount,
		FailedSources: failedCount,
		Platforms:     platforms,
	}

	fmt.Fprintf(os.Stderr, "\n[+] Scan complete: Found in %d/%d sources\n\n", foundCount, len(sources))

	return results
}

// HTTP client with timeout
var client = &http.Client{
	Timeout: 10 * time.Second,
	CheckRedirect: func(req *http.Request, via []*http.Request) error {
		return http.ErrUseLastResponse // Don't follow redirects
	},
}

func searchGoogle(phoneNumber string) Result {
	start := time.Now()
	result := Result{
		Source: "Google",
		URL:    fmt.Sprintf("https://www.google.com/search?q=%s", url.QueryEscape(phoneNumber)),
	}

	// Note: Google blocks automated searches
	result.Found = false
	result.Snippet = "Use generated Google dorks manually or configure Google API"
	result.ResponseTime = time.Since(start).Seconds()

	return result
}

func searchFacebook(phoneNumber string) Result {
	start := time.Now()
	result := Result{
		Source: "Facebook",
		URL:    fmt.Sprintf("https://www.facebook.com/search/top/?q=%s", url.QueryEscape(phoneNumber)),
	}

	resp, err := client.Get(result.URL)
	if err == nil {
		defer resp.Body.Close()
		result.Found = resp.StatusCode == 200
		if result.Found {
			result.Snippet = "Number may be searchable on Facebook (login required)"
		}
	} else {
		result.Error = err.Error()
	}

	result.ResponseTime = time.Since(start).Seconds()
	return result
}

func searchLinkedIn(phoneNumber string) Result {
	start := time.Now()
	result := Result{
		Source: "LinkedIn",
		URL:    fmt.Sprintf("https://www.linkedin.com/search/results/all/?keywords=%s", url.QueryEscape(phoneNumber)),
	}

	resp, err := client.Get("https://www.linkedin.com")
	if err == nil {
		defer resp.Body.Close()
		result.Found = false
		result.Snippet = "LinkedIn requires authentication for search"
	} else {
		result.Error = err.Error()
	}

	result.ResponseTime = time.Since(start).Seconds()
	return result
}

func searchTwitter(phoneNumber string) Result {
	start := time.Now()
	result := Result{
		Source: "Twitter/X",
		URL:    fmt.Sprintf("https://twitter.com/search?q=%s", url.QueryEscape(phoneNumber)),
	}

	result.Found = false
	result.Snippet = "Check Twitter manually or use API"
	result.ResponseTime = time.Since(start).Seconds()

	return result
}

func searchInstagram(phoneNumber string) Result {
	start := time.Now()
	result := Result{
		Source: "Instagram",
		URL:    fmt.Sprintf("https://www.instagram.com/explore/tags/%s/", strings.ReplaceAll(phoneNumber, "+", "")),
	}

	resp, err := client.Get(result.URL)
	if err == nil {
		defer resp.Body.Close()
		result.Found = resp.StatusCode == 200
		if result.Found {
			result.Snippet = "Hashtag exists, check manually for actual posts"
		}
	} else {
		result.Error = err.Error()
	}

	result.ResponseTime = time.Since(start).Seconds()
	return result
}

func checkTrueCaller(phoneNumber string) Result {
	start := time.Now()
	
	result := Result{
		Source: "TrueCaller",
		URL:    fmt.Sprintf("https://www.truecaller.com/search/us/%s", url.QueryEscape(phoneNumber)),
	}

	req, err := http.NewRequest("GET", result.URL, nil)
	if err != nil {
		result.Error = err.Error()
		result.ResponseTime = time.Since(start).Seconds()
		return result
	}

	req.Header.Set("User-Agent", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36")
	
	resp, err := client.Do(req)
	if err == nil {
		defer resp.Body.Close()
		result.Found = resp.StatusCode == 200
		if result.Found {
			result.Snippet = "Number may be listed on TrueCaller - check manually"
		}
	} else {
		result.Error = err.Error()
	}

	result.ResponseTime = time.Since(start).Seconds()
	return result
}

func searchPastebin(phoneNumber string) Result {
	start := time.Now()
	result := Result{
		Source: "Pastebin",
		URL:    fmt.Sprintf("https://psbdmp.ws/?q=%s", url.QueryEscape(phoneNumber)),
	}

	req, err := http.NewRequest("GET", result.URL, nil)
	if err != nil {
		result.Error = err.Error()
		result.ResponseTime = time.Since(start).Seconds()
		return result
	}

	req.Header.Set("User-Agent", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36")
	
	resp, err := client.Do(req)
	if err == nil {
		defer resp.Body.Close()
		body, _ := io.ReadAll(resp.Body)
		bodyStr := string(body)
		
		if strings.Contains(bodyStr, "No results") {
			result.Found = false
			result.Snippet = "No pastes found containing this number"
		} else if strings.Contains(bodyStr, phoneNumber) || strings.Contains(bodyStr, "results found") {
			result.Found = true
			result.Snippet = "Number found in paste dumps - check URL for details"
		}
	} else {
		result.Error = err.Error()
	}

	result.ResponseTime = time.Since(start).Seconds()
	return result
}

func searchGitHub(phoneNumber string) Result {
	start := time.Now()
	result := Result{
		Source: "GitHub",
		URL:    fmt.Sprintf("https://github.com/search?q=%s&type=code", url.QueryEscape(phoneNumber)),
	}

	resp, err := client.Get(result.URL)
	if err == nil {
		defer resp.Body.Close()
		body, _ := io.ReadAll(resp.Body)
		bodyStr := string(body)
		
		if strings.Contains(bodyStr, "We couldn't find any code matching") {
			result.Found = false
			result.Snippet = "No code found containing this number"
		} else if resp.StatusCode == 200 {
			result.Found = true
			result.Snippet = "Possible matches in code repositories - check manually"
		}
	} else {
		result.Error = err.Error()
	}

	result.ResponseTime = time.Since(start).Seconds()
	return result
}
