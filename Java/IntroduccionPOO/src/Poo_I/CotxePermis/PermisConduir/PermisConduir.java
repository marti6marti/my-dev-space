package Poo_I.CotxePermis.PermisConduir;

public class PermisConduir {

    private String nom;
    private String tipusPermis;
    private int punts;

    public void setNom(String nom){
        this.nom = nom;
    }

    public String getNom() {
        return nom;
    }

    public void setTipusPermis(String tipusPermis) {
        this.tipusPermis = tipusPermis;
    }

    public String getTipusPermis() {
        return tipusPermis;
    }

    public void setPunts(int punts) {
        this.punts = punts;
    }

    public int getPunts() {
        return punts;
    }

    public void imprimirPermis(){
        System.out.println(nom);
        System.out.println(tipusPermis);
        System.out.println(punts);
    }
    public void restarPunts(int punts){
        this.punts -= punts;
    }
}
