package de.getzler;

import java.util.Arrays;
import java.util.Random;

public class LottoMachine
{
    private final int[] lottoNumbers;

    public LottoMachine()
    {
        this.lottoNumbers = new int[6];
    }

    public int[] getLottoNumbers()
    {
        return lottoNumbers;
    }

    @Override public String toString()
    {
        StringBuilder builder = new StringBuilder();
        builder.append("Actual Lotto numbers are: ");
        for (int var : lottoNumbers)
        {
            builder.append(String.format("%2d", var) + " ");
        }
        return builder.toString();
    }

    public void resetNumbers()
    {
        Arrays.fill(lottoNumbers, 0);
    }

    public void makeNewNumbers()
    {
        while (Arrays.stream(lottoNumbers).anyMatch(i -> i == 0))
        {
            makeOneNumber();
        }
    }

    private void makeOneNumber()
    {
        boolean flag = true;
        while (flag)
        {
            Random random = new Random();
            int num = 1 + random.nextInt(49);
            if (Arrays.stream(lottoNumbers).noneMatch(i -> i == num))
            {
                for (int j = 0; j < lottoNumbers.length; j++)
                {
                    if (lottoNumbers[j] == 0)
                    {
                        lottoNumbers[j] = num;
                        flag = false;
                        break;
                    }
                }
            }
        }
    }
}