package Proyecto_Poo;

public class Profesor extends Persona{
    private String materia;

    public Profesor(String nom, int tel, String especialitzacio) {
        super(nom, tel);
        this.materia = especialitzacio;
    }

    public String getMateria() {
        return materia;
    }

    public void setMateria(String materia) {
        this.materia = materia;
    }

    @Override
    public String toString() {
        return "Profesor{" +
                "nom='" + getNom() + '\'' +
                ", tel=" + getTel() +
                ", materia='" + materia + '\'' +
                '}';
    }
}
