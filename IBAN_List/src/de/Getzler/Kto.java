package de.Getzler;

public class Kto
{
    private int seed;
    private int checksum;
    private int value;

    public Kto(int seed)
    {
        this.seed = seed;
        this.checksum = calculateCheck(seed);
        this.value = (seed * 10) + checksum;
    }

    private int calculateCheck(int seed)
    {
        // input check
        if (seed > 999999999 || seed < 1)
        {
            throw new NumberFormatException("Number must be from 1 to 999.999.999!");
        }

        // array initialization
        int[] arrayKto = initializeArray(seed);

        // check if Stelle 3 is a 9
        int j;
        if (arrayKto[2] == 9)
        {
            j = 7;
        }
        else
        {
            j = 6;
        }

        // calculation
        int m = 2;
        int sumOfProducts = 0;
        for (int i = 0; i < j; i++)
        {
            arrayKto[8 - i] = arrayKto[8 - i] * m;
            m++;
            sumOfProducts = sumOfProducts + arrayKto[8 - i];
        }

        // finalisation + return checksum
        int checksum = 11 - (sumOfProducts % 11);
        if ((sumOfProducts % 11 == 10) || (sumOfProducts % 11 == 0))
        {
            checksum = 0;
        }
        return checksum;
    }

    public int getValue()
    {
        return value;
    }

    public int[] initializeArray(int seed)
    {
        //123456789 Stelle
        //012345678 Array
        String temp = Integer.toString(seed);
        int[] arrayKto = new int[9];
        for (int i = 0; i < temp.length(); i++)
        {
            try
            {
                arrayKto[i + (9 - temp.length())] = temp.charAt(i) - '0';
            }
            catch (Exception e)
            {
            }
        }
        return arrayKto;
    }
}