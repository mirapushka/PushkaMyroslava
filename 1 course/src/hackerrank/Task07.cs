//https://www.hackerrank.com/challenges/breaking-best-and-worst-records
using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Collections;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using System.Text.RegularExpressions;
using System.Text;
using System;

class Result
{

    /*
     * Complete the 'breakingRecords' function below.
     *
     * The function is expected to return an INTEGER_ARRAY.
     * The function accepts INTEGER_ARRAY scores as parameter.
     */

    public static List<int> breakingRecords(List<int> scores)
    {
int maxRecord = scores[0];
        int minRecord = scores[0];
        int maxCount = 0;
        int minCount = 0;

        for (int i = 1; i < scores.Count; i++)
        {
            if (scores[i] > maxRecord)
            {
                maxRecord = scores[i];
                maxCount++;
            }
            else if (scores[i] < minRecord)
            {
                minRecord = scores[i];
                minCount++;
            }
        }

        List<int> result = new List<int>();
        result.Add(maxCount);
        result.Add(minCount);
        
        return result;
    }

}

class Solution
{
    public static void Main(string[] args)
    {
        TextWriter textWriter = new StreamWriter(@System.Environment.GetEnvironmentVariable("OUTPUT_PATH"), true);

        int n = Convert.ToInt32(Console.ReadLine().Trim());

        List<int> scores = Console.ReadLine().TrimEnd().Split(' ').ToList().Select(scoresTemp => Convert.ToInt32(scoresTemp)).ToList();

        List<int> result = Result.breakingRecords(scores);

        textWriter.WriteLine(String.Join(" ", result));

        textWriter.Flush();
        textWriter.Close();
    }
}
