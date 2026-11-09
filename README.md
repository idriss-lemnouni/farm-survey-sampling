# Sondage stratifié sur des poids de poussins

Comparaison de deux plans de sondage de 24 individus sur les 71 observations réelles de l’expérience chickwts. La moyenne des 71 poids sert de référence. Le programme compare 5 000 tirages sans remise par méthode, avec une graine fixe.

Le sondage stratifié répartit les places entre les six groupes d’alimentation proportionnellement à leurs effectifs, puis pondère chaque moyenne par le poids de sa strate. Le rapport compare le biais, la dispersion et la RMSE en grammes.

## Reproduction

Télécharger le [CSV chickwts](https://raw.githubusercontent.com/vincentarelbundock/Rdatasets/master/csv/datasets/chickwts.csv) dans le dossier du script sous le nom chickwts.csv. Exécuter `python sampling.py` avec Python 3. Le résultat figure dans results.json.

La [documentation officielle R](https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/chickwts.html) décrit l’expérience et cite sa source originale, l’ouvrage *Statistical Methods* de G. W. Snedecor et W. G. Cochran. Les mesures sont réelles. Les tirages sont simulés et illustrent la précision des deux plans sur cette population finie.
