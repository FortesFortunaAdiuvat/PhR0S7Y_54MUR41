using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Solution
{
    static void Main(string[] args)
    {
        string text = Console.ReadLine();

        // Write an answer using Console.WriteLine()
        // To debug: Console.Error.WriteLine("Debug messages...");

        for(var idx = 0; idx < text.Length; idx++){
            if('A' <= text[idx] && text[idx] <= 'Z')
                Console.Write(text[idx].ToString().ToLower());
        }
        Console.WriteLine();
    }
}