# Project 3 - Data GeoSpartial Project
![alt text](https://github.com/Macarena18/GeoSpartial-Data-Project/blob/master/INPUT/images2.jpg)

**Fuentes de datos:**
- Dataset `companies.json`
- Web Scrapping - *Report on 2019´s Best Cities for Gamers* -> http://blog.gisuser.com/2019/06/05/report-on-2019s-best-cities-for-gamers
- API - *Geocode* -> https://geocode.xyz/api
- API - *FourSquare* -> https://developer.foursquare.com/docs/api-reference/venues/explore/
- API - *GooglePlaces* -> https://developers.google.com/places/web-service/search

El **objetivo** del proyecto es tratar de encontrar la mejor localización para la apertura de nuevas oficinas de una empresa de Gaming. Para ello, la compañia requiere que se cumplen los siguientes requisitos:

- *Developers like to be near successful tech startups that have raised at least 1 Million dollars.*
- *Executives like Starbucks A LOT. Ensure there's a starbucks not to far.*
- *Account managers need to travel a lot.*
- *All people in the company have between 25 and 40 years, give them some place to go to party.*
- *The CEO is Vegan.*
- *Designers like to go to design talks and share knowledge. There must be some nearby companies that also do design.*
- *30% of the company have at least 1 child.*


Para ello, he seguido los siguientes pasos:

**Analysis Gaming Companies del Dataset:`AnalysisCity.ipynb`**

En primer lugar, realizo un análisis sobre las empresas de Gaming `category_code:games_video`que se encuentran dentro del dataset `companies.json` y las categorizo por **país y cuidad**, para poder identificar el país y las cuidades más populares para la apertura de oficinas en el sector. Tras analizar los datos, encuentro que **USA** es el país más solicitado.

Teniendo en cuenta estos datos, procedo a investigar a través de `Web Scrapping`cuales son las *cuidades top en USA para los gamers*. Tras analizar los resultados, **Seattle** es la cuidad top para los gamers en 2019, por lo que va a ser la cuidad escogida para la apertura de la próxima oficina de la compañia.

Dicho esto, procedo a filtrar en el dataset las compañias Gaming en la cuidad de Seattle. Con la ayuda de `Folium`, identifico un punto centrico de la cuidad **Midtown Seattle** y procedo a geolocalizar estas compañias en el mapa. `GamingCompanies_Seattle.html`

**Check Requirements: `CheckRequirements.ipynb`**

En segundo lugar, procedo a  verificar qué compañias del dataset cumplen con los requisitos  de localización que solicita la compañia. Para ello, seleccionamos todas las compañias tecnologicas que se encuentren en la cuidad de Seattle y filtramos por las que hayan generado más de un **1 millón de dólares**.

Por otro lado, con la ayuda de las apis `GooglePlaces`,`FourSquare`,`Geocode`, localizamos los siguientes establecimientos: (`API.py`)
- Starbucks
- Transportes (Metro, Estación de tren, Aeropuerto)
- Pubs
- Colegios
- Restaurantes Veganos

Una vez encontrados todos los requirimientos cercanos al punto céntrico establecido, generamos un **mapa** para visualizar como se distribuyen estos puntos:
`Tableau Map` https://public.tableau.com/profile/macarena6661#!/vizhome/RequirementsOfficesSeattleMap/Hoja1?publish=yes

**Office Location Election** `OfficeElectionAnalysis.ipynb`

Tras visualizar el mapa, seleccionamos las compañias y verificamos cuáles cumplen los siguientes requisitos con la ayuda de `Geospartial queries de Mongo`: 

- Starbucks cercano < 200 metros
- Varios restaurantes veganos cercanos < 200 metros
- Pubs cercanos < 500 metros
- Aeropuerto en un radio de 10000 km
- Colegio a menos de 5000 km


Finalmente, las coordenadas seleccionadas son las de la compañia **SynapticMash**:

**Latitude: 47.6098932**
**Longitude: -122.3379255**

Esta localización cumple con los siguientes requisitos: `office+requirements.png`

- Distance for **Starbucks** -> *180 meters*
- Distance for **Vegan restaurant** -> *97 meters*
- Distance for **Pubs** -> *207 meters*
- Distance for **Airport**-> *8429 kilometers*
- Distance for **School** -> *589 kilometers*


![Foto](https://github.com/Macarena18/GeoSpartial-Data-Project/blob/master/OUTPUT/location_office.png)


