using System;

namespace MyApp 
{
    class jm
    {
        public string Encrpyt(string plainText, long offset)
        {
            string b = "";
            char[] a = new char[100];
            for (int i = 0; i < plainText.Length; i++)
            {
                a[i] = plainText[i];
                if (plainText[i] >= 65 && plainText[i] <= 90)
                {
                    if ((int)a[i] + offset >90)
                        a[i] = (char)((int)a[i] - 26);
                    a[i] = (char)((int)a[i] + offset);
                }
                if (plainText[i] >= 97 && plainText[i] <= 122)
                {
                    if ((int)a[i] + offset >122)
                        a[i] = (char)((int)a[i] - 26);
                    a[i] = (char)((int)a[i] + offset);
                }
            }
            for (int i = 0; i < plainText.Length; i++)
                b += a[i];
            return b;
        }
    }
    internal class Program
    {
        static void Main(string[] args)
        {
            Random r = new Random();
            jm s = new jm();
            string p=Console.ReadLine();
            int ans = 0;
            string op = "";
            int pss = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(s.Encrpyt(p, pss));
            /*for (int i = 0; i <= 25; i++)
            {
                int a = 0;
                string sum = s.Encrpyt(p, i);
                for (int j = 0; j < sum.Length; j++)
                    if (sum[j] == 'e')
                        a++;
                if (ans < a)
                {
                    op = sum;
                    ans = a;
                }
            }
            Console.Write(op);*/
        }
    }
}