using System;
using System.Collections.Generic;
using System.Text;

namespace Практична_2._задача_Hackerrank._Staircase.src.hackerrank
{
    internal class TaskStaircase
    {
        public static void Solve(int n)
        {
            for (int i = 1; i <= n; i++)
            {
                string line = new string(' ', n - i) + new string('#', i);
                Console.WriteLine(line);
            }
        }
    }
}
