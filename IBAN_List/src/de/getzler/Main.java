package de.getzler;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class Main
{
    public static void main(String[] args)
    {
        File f = new File("IBAN-List.txt");
        f.delete();
        for (int i = 1; i < 100; i++)
        {
            try
            {
                IBAN myIban = new IBAN("DE", 131400, 73369920, new Kto(i));

                writeLinetoFile(f, myIban.getKtoValue() + " | " + myIban.getValue() + "\n");
            }
            catch (Exception e)
            {
                System.out.println(e);
            }
        }
    }

    public static void writeLinetoFile(File f, String s) throws IOException
    {
        FileWriter writer = new FileWriter(f, true);
        writer.write(s);
        writer.close();
    }
}
