//https://www.hackerrank.com/challenges/staircase/problem
using System;
class Result
{

    /*
     * Complete the 'staircase' function below.
     *
     * The function accepts INTEGER n as parameter.
     */

    public static void staircase(int n)
    {
for (int i = 1; i <= n; i++)
        {
            Console.WriteLine(new string(' ', n - i) + new string('#', i));
        }
    }

}
class Solution
{
    public static void Main(string[] args)
    {
        int n = Convert.ToInt32(Console.ReadLine().Trim());

        Result.staircase(n);
    }
}
