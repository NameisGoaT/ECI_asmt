from django.test import TestCase
from .models import Book

class BookModelTestCase(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            genre="Fiction",
            language="English",
            subjects="Test Subject",
            bookshelves="Test Bookshelf",
            download_links=["link1", "link2"],
            popularity=100,
            book_id=123,
            mime_type="text/plain"
        )

    def test_model_creation(self):
        self.assertIsInstance(self.book, Book)
        self.assertEqual(self.book.title, "Test Book")
        self.assertEqual(self.book.author, "Test Author")
        self.assertEqual(self.book.genre, "Fiction")
        self.assertEqual(self.book.language, "English")
        self.assertEqual(self.book.subjects, "Test Subject")
        self.assertEqual(self.book.bookshelves, "Test Bookshelf")
        self.assertEqual(self.book.download_links, ["link1", "link2"])
        self.assertEqual(self.book.popularity, 100)
        self.assertEqual(self.book.book_id, 123)
        self.assertEqual(self.book.mime_type, "text/plain")

    def test_string_representation(self):
        self.assertEqual(str(self.book), "Test Book")
