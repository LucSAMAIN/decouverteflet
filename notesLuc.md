# Apprentissage de Flet via la documentation officielle et gpt / copilot.
Chat(GPT) associé : https://chatgpt.com/c/6807d907-ad04-800f-849d-88eca895c8c3

Documentation officielle : htt  ps://flet.dev/docs/

## Installation et introduction:
### Installation et création d'un environnement virtuel pour flet
On a besoin d'un environnement Python:
```bash
python -m venv .venv
.venv\Scripts\activate
pip install flet[all]
flet --version # pour vérifier la version de flet
```

### Exécution d'un code Flet

Ensuite pour executer un code écrit avec Flet, il faut l'executer avec la commande suivante:
```bash
flet run <nom_du_fichier>.py
```
Voir le code 'counter.py' pour le premier exemple donné par la documentation officielle.
On peut ajouter l'option '--web' pour forcer l'ouverture dans le navigateur web(défault pour moi c'est chrome windows):
```bash
flet run counter.py --web
```

### Création d'une application Flet
Flet est un framework, donc on va plus souvent passer par la commande 'flet' pour correctement créer une application.
En gros, c'est pas du raw python code... Ya un peu de sucre syntaxique pour faire joli et plus simple !

```bash
flet create
```
Pour créer une app vierge.
```bash
flet run <nom_de_l_app>
``` 
va lancer le fichier 'main.py' de l'application qu'on vient de créer (voir le 'src').

A CHAQUE FOIS QU'ON MODIFIE LE CODE LANCE (ICI LE MAIN) ALORS IL Y A UN HOT RELOAD QUI SE FAIT AUTOMATIQUEMENT.




## Début de l'apppppprennntisssaggge
### Flet widgets !
Un widget est toujours inséré dans un widget parent ou une page. La page est donc la racine de tout arbre widget.
Un type de widget = une classe python.
Dans Flet on appelle ca dun "control".
On peut donc ajouter un control à une page par exemple(dans notre main page):
```python
# page.controls.append(counter)
# page.update()
# =
page.add(counter)
```

**Il faut toujours faire un 'page.update()' pour que les modifications soient prises en compte.**

### Flet containers:
Dont le seul but est de contenir d'autres widgets, exemple:
```python
page.add(
    ft.Row(controls=[
        ft.Text("A"),
        ft.Text("B"),
        ft.Text("C")
    ])
)
```

### Flet events:
Certains widgets peuvent réagir à des événements, par exemple le 'onclick' d'un bouton.

### Etc.
Pour en savoir plus sur les widget de base voir : https://flet.dev/docs/getting-started/flet-controls





## Custom controls:
On peut créer nos propre widgets en utilisant l'héritage !
Suffit de créer une classe héritant d'un widget de base pour pouvoir le customiser à notre guise. voir : https://flet.dev/docs/getting-started/custom-controls


## Flet adaptation:
https://flet.dev/docs/getting-started/adaptive-apps
En fonction de la plateforme (IOS, android) Flet adapte les widgets.
```python
page.adaptive = True
```
Alors par exemple si on est sur un IOS les rendus seront différents.
Cettre propriété peut aussi se régler au niveau d'un élément et pas la page en entier.

Mais parfois il faudra modifier notre custom element pour qu'il s'adpate exactement comme on le souhaite.
Comprendre que Flet ne saura pas exactement ce qu'on souhaite...
J'ai parlé de IOs et android mais on peut aussi pensé à la propriété `page.web`.


## Navigation and routing:
https://flet.dev/docs/getting-started/navigation-and-routing
