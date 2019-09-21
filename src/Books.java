public class Books
{
    private String bookName;
    private String authorName;
    private long ISBN;

    public String getAuthorName() {
        return authorName;
    }

    public void setAuthorName(String authorName) {
        this.authorName = authorName;
    }

    public long getISBN() {
        return ISBN;
    }

    public void setISBN(long ISBN) {
        this.ISBN = ISBN;
    }

    public String getBookName() {
        return bookName;
    }

    public void setBookName(String bookName) {
        this.bookName = bookName;
    }

    public void Books(String bookName,String authorName,long ISBN)
    {
        this.authorName=authorName;
        this.bookName=bookName;
        this.ISBN=ISBN;
    }
    @Override
    public String toString()
    {
        return "bookname"+bookName+"\nauthername"+authorName+"\n ISBN"+ISBN;
    }
}