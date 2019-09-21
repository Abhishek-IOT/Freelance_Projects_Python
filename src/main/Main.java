package main;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("enter the name of book");
        int n=sc.nextInt();
        String[] bookName =new String[n];
        String[] autherName =new String[n];
        long[] ISBN =new long[n];
        sc.nextLine();
        if(n==0)
            System.out.println("na");
        else
        {
            for(int i=0;i<n;i++)
            {
                bookName[i]=sc.nextLine();
                autherName[i]=sc.nextLine();
                ISBN[i]=sc.nextLong();
                sc.nextLine();

            }
        }
        for (int j=0;j<n;j++)
        {
            System.out.println("bookname\t"+bookName[j]+"\nauthorname\t"+autherName[j]+"\nISBN\t"+ISBN[j]);

        }
            }
}
