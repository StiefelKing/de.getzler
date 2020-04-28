package de.Getzler;

public class Main
{

    public static void main(String[] args)
    {
        long infected = Long.parseLong(args[0]);
        int weeks = Integer.parseInt(args[1]);
        double increaseRate = Double.parseDouble(args[2]) / 100;
        double mortality = Double.parseDouble(args[3]) / 100;
        long dead = 0;
        //infected = 100; weeks = 26; increaseRate = 0.255; mortality = 0.035;
        virusCalculator(infected, weeks, increaseRate, mortality);
    }

    public static void virusCalculator(long infected, int weeks, double increaseRate, double mortality)
    {
        System.out.println(" Week" + "   Infections" + "       Deaths");
        for (int i = 1; i <= weeks; i++)
        {
            long dead = Math.round(infected * mortality);
            System.out.println(String.format("%5d", i) + " " + String.format("%12d", infected) + " " + String.format("%12d", dead));
            infected = infected + Math.round(infected * increaseRate);
        }
    }
}