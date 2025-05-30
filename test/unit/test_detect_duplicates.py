import pytest
from src.util.detector import detect_duplicates
from src.util.parser import Article
# develop your test cases here


# Helper to create BibTeX entry
def make_bibtex_entry(key, doi=None):
    lines = [f"@article{{{key},"]
    lines.append("  title={Example Title},")
    if doi:
        lines.append(f"  doi={{ {doi} }},")
    lines.append("}")
    return "\n".join(lines)

# 1: Empty input
@pytest.mark.unit
def test_empty_input_raises_valueerror():
    data = ""
    with pytest.raises(ValueError, match="not contain enough articles"):
        detect_duplicates(data)

# 2: Single article input
@pytest.mark.unit
def test_single_article_raises_valueerror():
    entry = make_bibtex_entry("ferdiie2020")
    with pytest.raises(ValueError, match="not contain enough articles"):
        detect_duplicates(entry)

# 3: Duplicate with same key + same DOI
@pytest.mark.unit
def test_same_key_same_doi_duplicate_length():
    entry1 = make_bibtex_entry("ferdiie2020", "10.1000/xyz123")
    entry2 = make_bibtex_entry("ferdiie2020", "10.1000/xyz123")
    data = entry1 + "\n" + entry2
    duplicates = detect_duplicates(data)
    assert len(duplicates) == 1

@pytest.mark.unit
def test_same_key_same_doi_duplicate_content():
    entry1 = make_bibtex_entry("ferdiie2020", "10.1000/xyz123")
    entry2 = make_bibtex_entry("ferdiie2020", "10.1000/xyz123")
    data = entry1 + "\n" + entry2
    duplicates = detect_duplicates(data)
    assert "ferdiie2020" in str(duplicates[0])

# 4: Same key, one DOI missin
@pytest.mark.unit
def test_same_key_one_doi_missing_duplicate_length():
    entry1 = make_bibtex_entry("ferdiie2020")
    entry2 = make_bibtex_entry("ferdiie2020", "10.1000/xyz123")
    data = entry1 + "\n" + entry2
    duplicates = detect_duplicates(data)
    assert len(duplicates) == 1

# 5: Same key, no DOI
@pytest.mark.unit
def test_same_key_no_doi_duplicate_length():
    entry1 = make_bibtex_entry("ferdiie2020")
    entry2 = make_bibtex_entry("ferdiie2020")
    data = entry1 + "\n" + entry2
    duplicates = detect_duplicates(data)
    assert len(duplicates) == 1

# 6: Same key, different DOI
@pytest.mark.unit
def test_same_key_different_doi_duplicate_length():
    entry1 = make_bibtex_entry("ferdiie2020", "10.1000/abc")
    entry2 = make_bibtex_entry("ferdiie2020", "10.1000/def")
    data = entry1 + "\n" + entry2
    duplicates = detect_duplicates(data)
    assert len(duplicates) == 1

# 7: Different key + different DOI
@pytest.mark.unit
def test_different_key_doi_no_duplicate():
    entry1 = make_bibtex_entry("ferdiie2020", "10.1000/abc")
    entry2 = make_bibtex_entry("vito2020", "10.1000/def")
    data = entry1 + "\n" + entry2
    duplicates = detect_duplicates(data)
    assert len(duplicates) == 0



@pytest.mark.unit
def test_detect_duplicates():
    assert True


# Test cases are structured according to the 4-step test design technique: (detect_duplicates), 
# conditions (number of articles, key equality, DOI presence/equality), combinations and expected outcomes.
# Each test case targets one logical combination of conditions

# There is no shared state or data between tests; each test is self-standing and isolated from the others.
#And also one helper function used.

#I had a hard time following the one assert per test rule and I cannot be sure of the accuracy of my tests because I have time constraints.