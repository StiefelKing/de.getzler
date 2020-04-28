package de.Getzler;

import java.math.BigInteger;

public class IBAN
{
    private Kto kto;
    private String value;

    public IBAN(String country, int countryNum, int blz, Kto kto)
    {
        // assignments
        this.kto = kto;
        this.value = country;

        // formalizing
        BigInteger bKto = BigInteger.valueOf(kto.getValue()).multiply(new BigInteger("1000000"));
        BigInteger bBlz = BigInteger.valueOf(blz).multiply((new BigInteger("10000000000000000")));
        BigInteger bban = bBlz.add(bKto.add(BigInteger.valueOf(countryNum)));

        // calculation
        BigInteger pz;
        pz = BigInteger.valueOf(98).subtract(bban.mod(BigInteger.valueOf(97)));

        // output
        bban = bban.subtract(BigInteger.valueOf(countryNum));
        bban = bban.divide(new BigInteger("1000000"));
        this.value = this.value + String.format("%02d", pz) + bban;
    }

    public String getValue()
    {
        //format XX00 0000 0000 0000 0000 00
        return formatValue(this.value);
    }

    public String formatValue(String value)
    {
        int period = 4;
        StringBuilder builder = new StringBuilder(value.length() + value.length() * (value.length() / period) + 1);
        int index = 0;
        String prefix = "";
        while (index < value.length())
        {
            builder.append(prefix);
            prefix = " ";
            builder.append(value, index, Math.min(index + period, value.length()));
            index += period;
        }
        return builder.toString();
    }

    public String getKtoValue()
    {
        return String.format("%010d", kto.getValue());
    }
}