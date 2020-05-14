package de.getzler;

public class LottoMachineTester
{
    public static void main(String[] args)
    {
        LottoMachine myLotto = new LottoMachine();
        myLotto.makeNewNumbers();
        System.out.println(myLotto.toString());
        myLotto.resetNumbers();
        myLotto.makeNewNumbers();
        System.out.println(myLotto.toString());
    }
}
