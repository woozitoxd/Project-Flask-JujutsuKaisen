from flask import Flask, render_template, url_for

app = Flask(__name__)

# Datos que se mandan a la plantilla
character_data = {
    # Tu diccionario original
}

characters = [
    {
        "id": "yuji",
        "name": "Yuji Itadori",
        "age": 15,
        "type": "Hechicero",
        "grade": "1er Año",
        "affiliation": "Escuela Técnica de Jujutsu de Tokio",
        "technique": "Recipiente de Sukuna / Fuerza sobrehumana",
        "image": "yuji.webp",
        "bio": [
            "Yuji Itadori es un estudiante de secundaria con una fuerza física excepcional. Tras la muerte de su abuelo, se une al Club de Ocultismo de su escuela donde encuentra un objeto maldito de alto nivel: un dedo del legendario Ryomen Sukuna.",
            "Para salvar a sus amigos de una maldición, Itadori ingiere el dedo, convirtiéndose en el recipiente de Sukuna. Aunque normalmente esto significaría una sentencia de muerte inmediata, Gojo Satoru ve el potencial en Itadori y lo inscribe en la Escuela Técnica de Jujutsu de Tokio.",
            "A pesar de ser inexperto, Itadori posee un fuerte sentido de la justicia y un deseo innato de ayudar a los demás, incluso a costa de su propia vida."
        ],
        "moments": [
            "Combate contra la maldición especial en el edificio abandonado",
            "Primer intercambio con Sukuna",
            "Entrenamiento con Gojo Satoru",
            "Primer uso de Black Flash contra Mahito"
        ]
    },
    {
        "id": "megumi",
        "name": "Megumi Fushiguro",
        "age": 15,
        "type": "Hechicero",
        "grade": "1er Año",
        "affiliation": "Escuela Técnica de Jujutsu de Tokio",
        "technique": "Técnica de las Diez Sombras",
        "image": "megumi.webp",
        "bio": [
            "Megumi Fushiguro es un estudiante de primer año que proviene de la prestigiosa familia Zenin, conocida por sus poderosas técnicas de maldición.",
            "Es serio y reservado, pero tiene un fuerte sentido de la justicia. A diferencia de muchos hechiceros, Megumi no salva a las personas por gloria o prestigio, sino porque cree que las personas buenas merecen ser salvadas.",
            "Utiliza la Técnica de las Diez Sombras, que le permite invocar y controlar criaturas sombrías basadas en los Diez Tesoros Sagrados."
        ],
        "moments": [
            "Primer encuentro con Yuji Itadori",
            "Invocación de Nue contra Sukuna",
            "Combate contra la maldición en el centro comercial de Jujutsu Tech",
            "Desbloqueo de Mahoraga durante el Incidente de Shibuya"
        ]
    },
    {
        "id": "nobara",
        "name": "Nobara Kugisaki",
        "age": 16,
        "type": "Hechicera",
        "grade": "1er Año",
        "affiliation": "Escuela Técnica de Jujutsu de Tokio",
        "technique": "Técnica del Martillo y los Clavos",
        "image": "nobara.webp",
        "bio": [
            "Nobara Kugisaki es una joven proveniente de un pueblo rural que llegó a Tokio con grandes ambiciones. Determinada y confiada, no teme expresar sus opiniones.",
            "Su técnica maldita utiliza un martillo y clavos para atacar a las maldiciones a distancia, creando conexiones entre objetos vinculados y aprovechando conceptos de muñecas vudú.",
            "A pesar de su actitud desafiante, posee un fuerte sentido de la justicia y una determinación inquebrantable que la convierte en una poderosa aliada en combate."
        ],
        "moments": [
            "Demostración de su técnica en el examen de ingreso",
            "Batalla contra las hermanas malditas en el edificio abandonado",
            "Confrontación con Momo Nishimiya durante el Torneo de Intercambio",
            "Batalla contra Mahito durante el Incidente de Shibuya"
        ]
    },
    {
        "id": "gojo",
        "name": "Satoru Gojo",
        "age": 28,
        "type": "Hechicero",
        "grade": "Especial",
        "affiliation": "Escuela Técnica de Jujutsu de Tokio",
        "technique": "Técnica del Vacío Ilimitado / Seis Ojos",
        "image": "satoru_gojo.webp",
        "bio": [
            "Satoru Gojo es considerado el hechicero más poderoso del mundo. Posee la Técnica del Vacío Ilimitado y los Seis Ojos, una combinación que lo hace prácticamente invencible.",
            "Nacido en la prestigiosa familia Gojo, Satoru posee un carácter despreocupado y juguetón que contrasta con su inmensa fuerza. Como profesor de la Escuela Técnica de Jujutsu, guía a los estudiantes con métodos poco ortodoxos pero efectivos.",
            "A pesar de su actitud relajada, Gojo tiene una visión revolucionaria para el mundo de la hechicería y trabaja para cambiar las estructuras anticuadas de poder."
        ],
        "moments": [
            "Demostración de Púrpura contra Jogo",
            "Batalla contra Toji Fushiguro",
            "Revelación de la Expansión de Dominio: Vacío Ilimitado",
            "Enfrentamiento contra Sukuna durante el Incidente de Shibuya"
        ]
    },
    {
        "id": "sukuna",
        "name": "Ryomen Sukuna",
        "age": "Más de 1000",
        "type": "Maldición",
        "grade": "Especial",
        "affiliation": "Ninguna (Rey de las Maldiciones)",
        "technique": "Técnicas de Descuartizamiento / Llamas",
        "image": "sukuna.webp",
        "bio": [
            "Conocido como el 'Rey de las Maldiciones', Sukuna fue un hechicero durante la Era Dorada de la Hechicería hace más de 1000 años. Tras su muerte, se convirtió en una maldición tan poderosa que su cuerpo tuvo que ser desmembrado en 20 dedos.",
            "Tras ingerir Yuji uno de sus dedos, Sukuna reside dentro del cuerpo del joven, manteniendo una conciencia separada y ocasionalmente tomando el control.",
            "Posee un poder inmenso y cruel, sin consideración alguna por la vida humana. Su objetivo es recuperar todos sus dedos y reclamar su posición como la maldición más poderosa."
        ],
        "moments": [
            "Primera posesión del cuerpo de Yuji",
            "Batalla contra Megumi Fushiguro",
            "El pacto con Yuji",
            "Demostración de poder contra Jogo"
        ]
    },
    {
        "id": "maki",
        "name": "Maki Zenin",
        "age": 16,
        "type": "Hechicera",
        "grade": "4to Año",
        "affiliation": "Escuela Técnica de Jujutsu de Tokio",
        "technique": "Especialista en Armas / Fuerza Física",
        "image": "maki.webp",
        "bio": [
            "Maki Zenin proviene de la prestigiosa familia Zenin, pero nació sin energía maldita, lo que la convirtió en una paria dentro de su propio clan.",
            "A pesar de esta limitación, Maki posee una fuerza física extraordinaria y una habilidad excepcional en el manejo de armas malditas, convirtiéndola en una combatiente formidable.",
            "Su determinación para probar su valía a su familia y a sí misma la impulsa a convertirse en una de las mejores estudiantes de la Escuela Técnica de Jujutsu de Tokio."
        ],
        "moments": [
            "Demostración de habilidades durante el entrenamiento de primer año",
            "Batalla junto a Mai contra Mechamaru",
            "Combate contra las maldiciones durante el Torneo de Intercambio",
            "Enfrentamiento con su familia después del Incidente de Shibuya"
        ]
    }]

for id, data in character_data.items():
    character = {
        "id": id,
        "name": data["name"],
        "age": data["age"],
        "type": data["type"],
        "grade": data["grade"],
        "affiliation": data["affiliation"],
        "technique": data["technique"],
        "image": data["image"],
        "bio": data["bio"],
        "moments": data["moments"]
    }
    characters.append(character)

videos = [
    {
        "title": "Opening 1 - Kaikai Kitan",
        "description": "Primer opening de la serie",
        "url": "https://www.youtube.com/embed/1tk1pqwrOys"
    },
    {
        "title": "Trailer oficial",
        "description": "Trailer de lanzamiento",
        "url": "https://youtu.be/aPBUUJbrAWo"
    }
]

@app.route("/")
def home():
    nav_items = [
    {"name": "Personajes", "href": "#character-section"},
    {"name": "Videos", "href": "#videos-section"},
    {"name": "Manga", "href": "#"}
]
    return render_template("index.html", characters=characters, videos=videos, nav_items=nav_items)




if __name__ == "__main__":
    app.run(debug=True)
