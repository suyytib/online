using System;

namespace MyApp 
{
    class jm
    {
        public string Decrypt(string cipherText, long offset)
        {
            string b = "";
            char[] a = new char[100];
            for (int i = 0; i < cipherText.Length; i++)
            {
                a[i] = cipherText[i];
                if (cipherText[i] >= 65 && cipherText[i] <= 90)
                {
                    if ((int)a[i] - offset < 65)
                        a[i] = (char)((int)a[i] + 26);
                    a[i] = (char)((int)a[i] - offset);
                }
                if (cipherText[i] >= 97 && cipherText[i] <= 122)
                {
                    if ((int)a[i] - offset < 97)
                        a[i] = (char)((int)a[i] + 26);
                    a[i] = (char)((int)a[i] - offset);
                }
            }
            for (int i = 0; i < cipherText.Length; i++)
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
            for (int j = 0; j <25; j++)
            {
                int pss = Convert.ToInt32(Console.ReadLine());
                if (pss == -1)
                    break;
                Console.WriteLine(s.Decrypt(p, pss));
            }
            /*for (int i = 0; i <= 36; i++)
            {
                string sum = "";
                long sa = r.NextInt64(26);
                int a = 0;
                sum = s.Decrypt(p, sa);
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