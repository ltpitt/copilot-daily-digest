#!/usr/bin/env python3
"""
Comprehensive test suite for the metadata tracking system.

This script validates all functionality of the metadata system:
- Hash calculation and consistency
- Duplicate detection (videos and blog URLs)
- Change detection
- Metadata persistence
- Timestamp utilities
- Error handling

Run with: python scraper/test_metadata_system.py
"""

import sys
from pathlib import Path


# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from metadata import (
    add_blog_url,
    add_video_id,
    calculate_hash,
    get_changes_summary,
    get_current_timestamp,
    is_content_changed,
    is_newer_than,
    load_metadata,
    reset_metadata,
    update_content_hash,
)


class TestResults:
    """Track test results"""

    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.errors = []

    def add_pass(self, test_name):
        self.passed += 1
        print(f"  ✓ {test_name}")

    def add_fail(self, test_name, error):
        self.failed += 1
        self.errors.append((test_name, error))
        print(f"  ✗ {test_name}: {error}")

    def summary(self):
        total = self.passed + self.failed
        print(f"\n{'=' * 60}")
        print(f"Test Results: {self.passed}/{total} passed")
        if self.failed > 0:
            print("\nFailed tests:")
            for name, error in self.errors:
                print(f"  - {name}: {error}")
        print(f"{'=' * 60}")
        return self.failed == 0


results = TestResults()


def test_hash_calculation():
    """Test 1: Hash calculation and consistency"""
    print("\n[TEST 1] Hash Calculation")
    print("-" * 60)

    try:
        # Test consistency
        content = "Test content for hashing"
        hash1 = calculate_hash(content)
        hash2 = calculate_hash(content)

        if hash1 != hash2:
            results.add_fail("Hash consistency", f"Hashes differ: {hash1} != {hash2}")
            return
        results.add_pass("Hash consistency check")

        # Test hash length (SHA256 = 64 hex chars)
        if len(hash1) != 64:
            results.add_fail("Hash length", f"Expected 64 chars, got {len(hash1)}")
            return
        results.add_pass("Hash length validation (64 chars)")

        # Test different content produces different hash
        content2 = "Different content"
        hash3 = calculate_hash(content2)

        if hash1 == hash3:
            results.add_fail("Hash uniqueness", "Different content produced same hash")
            return
        results.add_pass("Different content produces different hashes")

        # Test empty string
        empty_hash = calculate_hash("")
        if len(empty_hash) != 64:
            results.add_fail("Empty string hash", f"Invalid hash length: {len(empty_hash)}")
            return
        results.add_pass("Empty string hashing")

    except Exception as e:
        results.add_fail("Hash calculation", str(e))


def test_metadata_loading():
    """Test 2: Metadata loading and creation"""
    print("\n[TEST 2] Metadata Loading")
    print("-" * 60)

    try:
        # Reset for clean state
        reset_metadata()
        results.add_pass("Metadata reset")

        # Load metadata
        metadata = load_metadata()

        # Check structure
        required_keys = [
            "version",
            "last_updated",
            "content_hashes",
            "video_ids",
            "blog_urls",
            "doc_versions",
            "stats",
        ]
        for key in required_keys:
            if key not in metadata:
                results.add_fail("Metadata structure", f"Missing key: {key}")
                return
        results.add_pass("Metadata has all required keys")

        # Check stats structure
        stats_keys = ["total_docs", "total_blog_posts", "total_videos", "last_successful_scrape"]
        for key in stats_keys:
            if key not in metadata["stats"]:
                results.add_fail("Stats structure", f"Missing stats key: {key}")
                return
        results.add_pass("Stats have all required keys")

        # Check version
        if metadata["version"] != "1.0.0":
            results.add_fail("Version", f"Expected 1.0.0, got {metadata['version']}")
            return
        results.add_pass("Version is correct (1.0.0)")

    except Exception as e:
        results.add_fail("Metadata loading", str(e))


def test_duplicate_detection():
    """Test 3: Duplicate detection for videos and blog URLs"""
    print("\n[TEST 3] Duplicate Detection")
    print("-" * 60)

    try:
        # Reset for clean state
        reset_metadata()

        # Test video ID - first add
        is_new = add_video_id("test_video_123")
        if not is_new:
            results.add_fail("Video ID first add", "Should return True for new video")
            return
        results.add_pass("New video ID added (returns True)")

        # Test video ID - duplicate
        is_new = add_video_id("test_video_123")
        if is_new:
            results.add_fail("Video ID duplicate", "Should return False for duplicate")
            return
        results.add_pass("Duplicate video ID rejected (returns False)")

        # Verify video is in metadata
        metadata = load_metadata()
        if "test_video_123" not in metadata["video_ids"]:
            results.add_fail("Video ID storage", "Video ID not found in metadata")
            return
        results.add_pass("Video ID stored in metadata")

        # Test blog URL - first add
        test_url = "https://github.blog/test-post"
        is_new = add_blog_url(test_url)
        if not is_new:
            results.add_fail("Blog URL first add", "Should return True for new URL")
            return
        results.add_pass("New blog URL added (returns True)")

        # Test blog URL - duplicate
        is_new = add_blog_url(test_url)
        if is_new:
            results.add_fail("Blog URL duplicate", "Should return False for duplicate")
            return
        results.add_pass("Duplicate blog URL rejected (returns False)")

        # Verify URL is in metadata
        metadata = load_metadata()
        if test_url not in metadata["blog_urls"]:
            results.add_fail("Blog URL storage", "Blog URL not found in metadata")
            return
        results.add_pass("Blog URL stored in metadata")

        # Test stats update
        if metadata["stats"]["total_videos"] != 1:
            results.add_fail("Video stats", f"Expected 1, got {metadata['stats']['total_videos']}")
            return
        results.add_pass("Video stats updated correctly")

        if metadata["stats"]["total_blog_posts"] != 1:
            results.add_fail(
                "Blog stats", f"Expected 1, got {metadata['stats']['total_blog_posts']}"
            )
            return
        results.add_pass("Blog post stats updated correctly")

    except Exception as e:
        results.add_fail("Duplicate detection", str(e))


def test_change_detection():
    """Test 4: Content change detection"""
    print("\n[TEST 4] Change Detection")
    print("-" * 60)

    try:
        # Reset for clean state
        reset_metadata()

        content_v1 = "Original content version 1"
        content_v2 = "Modified content version 2"
        file_path = "test/sample.md"

        # First check - new content should be detected as changed
        is_changed = is_content_changed(file_path, content_v1)
        if not is_changed:
            results.add_fail("New content detection", "New content should be detected as changed")
            return
        results.add_pass("New content detected as changed")

        # Update hash
        update_content_hash(file_path, content_v1)
        results.add_pass("Content hash updated")

        # Check same content - should NOT be changed
        is_changed = is_content_changed(file_path, content_v1)
        if is_changed:
            results.add_fail("Unchanged content", "Same content should not be detected as changed")
            return
        results.add_pass("Unchanged content correctly identified")

        # Check modified content - should be changed
        is_changed = is_content_changed(file_path, content_v2)
        if not is_changed:
            results.add_fail("Modified content", "Modified content should be detected as changed")
            return
        results.add_pass("Modified content detected as changed")

        # Verify hash is stored
        metadata = load_metadata()
        if file_path not in metadata["content_hashes"]:
            results.add_fail("Hash storage", "Hash not found in metadata")
            return
        results.add_pass("Content hash stored in metadata")

        # Verify hash matches
        stored_hash = metadata["content_hashes"][file_path]
        expected_hash = calculate_hash(content_v1)
        if stored_hash != expected_hash:
            results.add_fail(
                "Hash verification", f"Stored hash doesn't match: {stored_hash} != {expected_hash}"
            )
            return
        results.add_pass("Stored hash matches calculated hash")

    except Exception as e:
        results.add_fail("Change detection", str(e))


def test_doc_versions():
    """Test 5: Document version tracking"""
    print("\n[TEST 5] Document Version Tracking")
    print("-" * 60)

    try:
        # Reset for clean state
        reset_metadata()

        # Update a doc file
        doc_path = "docs/test-doc.md"
        content_v1 = "Documentation version 1"
        update_content_hash(doc_path, content_v1)

        # Check doc_versions is created
        metadata = load_metadata()
        doc_name = "test-doc"

        if doc_name not in metadata["doc_versions"]:
            results.add_fail("Doc version creation", f"Version not tracked for {doc_name}")
            return
        results.add_pass("Document version tracking initialized")

        # Check version structure
        doc_version = metadata["doc_versions"][doc_name]
        if "current_hash" not in doc_version:
            results.add_fail("Version structure", "Missing current_hash")
            return
        if "last_changed" not in doc_version:
            results.add_fail("Version structure", "Missing last_changed")
            return
        results.add_pass("Version structure complete")

        # Update to new version
        content_v2 = "Documentation version 2"
        update_content_hash(doc_path, content_v2)

        # Check previous_hash is stored
        metadata = load_metadata()
        doc_version = metadata["doc_versions"][doc_name]

        if "previous_hash" not in doc_version or doc_version["previous_hash"] is None:
            results.add_fail("Version history", "Previous hash not stored")
            return
        results.add_pass("Previous version hash stored")

        # Verify hashes
        if doc_version["current_hash"] == doc_version["previous_hash"]:
            results.add_fail("Version hashes", "Current and previous hash should differ")
            return
        results.add_pass("Current and previous hashes differ correctly")

    except Exception as e:
        results.add_fail("Document version tracking", str(e))


def test_timestamp_utilities():
    """Test 6: Timestamp utilities"""
    print("\n[TEST 6] Timestamp Utilities")
    print("-" * 60)

    try:
        # Get current timestamp
        timestamp = get_current_timestamp()

        # Check format
        if not timestamp.endswith("Z"):
            results.add_fail("Timestamp format", "Should end with Z (UTC)")
            return
        results.add_pass("Timestamp ends with Z (UTC)")

        if "T" not in timestamp:
            results.add_fail("Timestamp format", "Should contain T separator")
            return
        results.add_pass("Timestamp contains T separator (ISO 8601)")

        # Test is_newer_than
        is_recent = is_newer_than(timestamp, days=7)
        if not is_recent:
            results.add_fail("Recent timestamp check", "Current timestamp should be within 7 days")
            return
        results.add_pass("Current timestamp identified as recent")

        # Test old timestamp
        old_timestamp = "2020-01-01T00:00:00Z"
        is_recent = is_newer_than(old_timestamp, days=7)
        if is_recent:
            results.add_fail("Old timestamp check", "2020 timestamp should not be within 7 days")
            return
        results.add_pass("Old timestamp identified correctly")

        # Test with different day ranges
        is_recent_24h = is_newer_than(timestamp, days=1)
        if not is_recent_24h:
            results.add_fail("24h timestamp check", "Current timestamp should be within 24 hours")
            return
        results.add_pass("24-hour timestamp check works")

        # Test None/empty
        is_recent = is_newer_than(None, days=7)
        if is_recent:
            results.add_fail("None timestamp", "None should return False")
            return
        results.add_pass("None timestamp handled correctly")

    except Exception as e:
        results.add_fail("Timestamp utilities", str(e))


def test_changes_summary():
    """Test 7: Changes summary generation"""
    print("\n[TEST 7] Changes Summary")
    print("-" * 60)

    try:
        # Reset and add some data
        reset_metadata()

        add_video_id("video1")
        add_video_id("video2")
        add_blog_url("https://test.com/post1")
        update_content_hash("docs/doc1.md", "Doc content 1")
        update_content_hash("docs/doc2.md", "Doc content 2")

        # Get summary
        summary = get_changes_summary()

        # Check required keys
        required_keys = [
            "last_updated",
            "total_docs",
            "total_videos",
            "total_blog_posts",
            "last_successful_scrape",
        ]
        for key in required_keys:
            if key not in summary:
                results.add_fail("Summary keys", f"Missing key: {key}")
                return
        results.add_pass("Summary contains all required keys")

        # Check counts
        if summary["total_videos"] != 2:
            results.add_fail("Video count", f"Expected 2, got {summary['total_videos']}")
            return
        results.add_pass("Video count correct (2)")

        if summary["total_blog_posts"] != 1:
            results.add_fail("Blog count", f"Expected 1, got {summary['total_blog_posts']}")
            return
        results.add_pass("Blog post count correct (1)")

        if summary["total_docs"] != 2:
            results.add_fail("Doc count", f"Expected 2, got {summary['total_docs']}")
            return
        results.add_pass("Document count correct (2)")

        # Check tracked files
        if summary["tracked_files"] != 2:
            results.add_fail("Tracked files", f"Expected 2, got {summary['tracked_files']}")
            return
        results.add_pass("Tracked files count correct (2)")

    except Exception as e:
        results.add_fail("Changes summary", str(e))


def test_persistence():
    """Test 8: Data persistence across loads"""
    print("\n[TEST 8] Data Persistence")
    print("-" * 60)

    try:
        # Reset and add data
        reset_metadata()

        test_video = "persist_video_xyz"
        test_url = "https://persist.test/post"
        test_path = "persist/file.md"
        test_content = "Persist test content"

        add_video_id(test_video)
        add_blog_url(test_url)
        update_content_hash(test_path, test_content)

        # Load metadata fresh
        metadata = load_metadata()

        # Verify all data persisted
        if test_video not in metadata["video_ids"]:
            results.add_fail("Video persistence", "Video ID not persisted")
            return
        results.add_pass("Video ID persisted correctly")

        if test_url not in metadata["blog_urls"]:
            results.add_fail("URL persistence", "Blog URL not persisted")
            return
        results.add_pass("Blog URL persisted correctly")

        if test_path not in metadata["content_hashes"]:
            results.add_fail("Hash persistence", "Content hash not persisted")
            return
        results.add_pass("Content hash persisted correctly")

        # Verify hash value
        stored_hash = metadata["content_hashes"][test_path]
        expected_hash = calculate_hash(test_content)
        if stored_hash != expected_hash:
            results.add_fail("Hash value persistence", "Hash value incorrect after reload")
            return
        results.add_pass("Hash value persisted correctly")

    except Exception as e:
        results.add_fail("Data persistence", str(e))


def run_all_tests():
    """Run all tests"""
    print("=" * 60)
    print("METADATA TRACKING SYSTEM - COMPREHENSIVE TEST SUITE")
    print("=" * 60)

    try:
        # Run all tests
        test_hash_calculation()
        test_metadata_loading()
        test_duplicate_detection()
        test_change_detection()
        test_doc_versions()
        test_timestamp_utilities()
        test_changes_summary()
        test_persistence()

        # Show summary
        success = results.summary()

        if success:
            print("\n✅ ALL TESTS PASSED!")
            print("\nMetadata system is fully functional and ready to use.")

            # Show final state
            print("\nFinal Metadata State:")
            summary = get_changes_summary()
            for key, value in summary.items():
                print(f"  {key}: {value}")
        else:
            print("\n❌ SOME TESTS FAILED")
            print("\nPlease review the failures above and fix issues.")

        return success

    except Exception as e:
        print(f"\n❌ FATAL ERROR: {e}")
        import traceback

        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
