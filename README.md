# HTML Matcher

The pypi package in Python contains a series of functions for calculating the similarity ratio between pages in websites
or web applications.

## How to INSTALL?

```
pip install html-matcher
```

## How to USE?

By comparing the HTML structure, style, or both, the similarity ratio can be computed. Two techniques are available for
structure comparison: Matching Subsequences (MS) and All Path Tree Edit Distance (APTED). One algorithm that uses the
jaccard similarity metric is offered for style comparison.

### Structure

#### MS

#### Example

```
ms = MatchingSubsequences()
ratio = ms.similarity(page1,page2)
```

or you can use our improved method of MS that provides better results

```
ms = MatchingSubsequencesOptimized()
ratio = ms.similarity(page1,page2)
```

#### APTED

#### Example

```
apted = AllPathTreeEditDistance()
ratio = apted.similarity(page1,page2)
```

or you can use our improved method of APTED that reduces computational time

```
apted = AllPathTreeEditDistanceOptimized()
ratio = apted.similarity(page1,page2)
```

### Style

Each html document's css classes are extracted, and the **jaccard similarity** of the sets of classes is calculated.

#### Jaccard Similarity

```
J(A,B) = |A ∩ B| / |A U B|
```

#### Example

```
style = StyleSimilarity()
ratio = style.similarity(page1,page2)
```

### Structure & Style

We must pass a weight for each metric when combining similarity measures (k). The default value is 0.5, but in our
experiments, we found that, when comparing web pages based on their similarity ratio, structure takes precedence over
style, so 0.7 produces better results.

```
k * similarity(page_1, page_2) + (1 - k) * similarity(page_1, page_2)
```

#### Example

```
style = StyleSimilarity()
apted = AllPathTreeEditDistanceOptimized()
method = MixedSimilarity(apted, style, k=0.7)
ratio = method.similarity(page1,page2)
```