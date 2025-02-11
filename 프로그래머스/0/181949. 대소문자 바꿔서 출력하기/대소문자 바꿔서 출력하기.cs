using System;

public class Example
{
    public static void Main()
    {
        String s;
        String res = "";

        Console.Clear();
        s = Console.ReadLine();
        
        foreach(char elem in s){
            if('A' <= elem && elem <= 'Z'){
                res += (char)(elem + 32);
            }
            else{
                res += (char)(elem - 32);
            }
        }
        Console.WriteLine(res);
    }
}