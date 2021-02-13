# dialogflow-gcp-functions

Test de l'enregistrement d'une simple google cloud function en python qui expose un endpoint rest https://us-central1-southern-unity-304118.cloudfunctions.net/dialogflow-gcp-functions

**Pré-requis**:
 - avoir le google cloud SDK d'installé ou au minimum le cli gcloud
 - avoir un compte gcp et être loggé
 - avoir lié le repository github https://github.com/fbellame/dialogflow-gcp-functions au https://cloud.google.com/source-repositories de votre projet gcp
- avoir activé les google cloud functions dans gcp

Pour enregistrer la fonction:
```sh
./register-cloud-function.sh
```

Pour tester la fonction:
```sh
./test.sh
```
