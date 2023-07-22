# RESERVAS DE HOTEL

## Indice

I. [Descripción](#i-descripcion)   
II. [Instalacion con Docker](#ii-instalacion-con-docker)  
III. [Documentacion de las APIs](#iii-documentacion-de-las-apis)  
- [Endpoints](#endpoints)
      1. [Endpoint 1](#1-endpoint-1)
      2. [Endpoint 2](#2-endpoint-2)  
IV. [Testing](#iv-testing)  
V. [Convenciones texto a mostrar](#v-convenciones)  

## I. DESCRIPCION
Desarrollado con Django DRF con APIs REST, para la gestion de usuarios (user), cuartos (room), reservas (booking) y facturacion(invoice).

Arquitectura : Realizado de acuerdo Django MVC o MVT.  
Estructura de proyecto :

- hotel_v1/  Contiene la configuracion general del proyecto
- apps/ Contiene los diferentes modulos (user,room,booking, invoice)
  - base/ contiene el modelo general del cual hereda los demas para contener datos comunes para auditoria. 
  - user/ contiene el modelo, la vista y el serializados, asi como librerias utilitarios para el modulo. 
    - tests/ Contiene el base.py, factory.py para generar datos prueba y los tests respectivos.
- htmlcov/ Cobertura de codigo de acuerdo a los tests (coverage) [index.html](htmlcov%2Findex.html).    

Base de datos : Para fines didacticos se uso la base de datos relacional SQLlite.      
Autenticacion de usuario : JWT (JSON web token).  
Manejo de contenedores : Docker el archivo para despliegue esta en [Dockerfile](Dockerfile).  
Envio de correos electronicos : se configuro de forma Simple el envio de correos (send_mail) por cada reserva .  
Despliegue : Infraestructura en nube con AWS EC2 disponible en http://ec2-3-144-82-130.us-east-2.compute.amazonaws.com  
Documentacion: Se uso swagger para documentar los diferentes endpoints disponibles.

## III. Proceso Principal

### Endpoints
Comentario

#### 1. Crear un nuevo usuario

Descripción breve de lo que hace este endpoint y qué datos se deben enviar en las solicitudes.

- POST : {{base_url}}/users/register/
- Request :
 ```
curl --location 'http://localhost:8000/api/users/' \
--header 'Content-Type: application/json' \
--data-raw '{
  "username": "hernan.chambi4",
  "email": "hernan.chambi3@example.com4",
  "name": "hernan4",
  "last_name": "chambi4",
  "password": "password123",
  "nit": "5256230122"
}
' 
 ```
- Response :
 ```
{
  "username": "hernan.chambi",
  "email": "hernan.chambi3@example.com",
  "name": "hernan",
  "last_name": "chambi",
  "password": "password123",
  "nit": "5256230122"
}
 ```

#### 2. Endpoint 2

Descripción breve de lo que hace este endpoint y qué datos se deben enviar en las solicitudes.

- POST : {{base_url}}/rooms/ 
- Request:
 ```
curl --location 'http://localhost:8000/api/rooms/' \
--header 'Content-Type: application/json' \
--data '{
  "type": "SIM",
  "description": "Habitación simple con vista al lago4",
  "price_per_day": 100.50,
  "discount_rate": 10,
  "is_available": true
}
'
 ```
- Response :
 ```
{
  "type": "SIM",
  "description": "Habitación simple con vista al lago",
  "price_per_day": 100.50,
  "discount_rate": 10,
  "is_available": true
}
 ```
3. Realizar una nueva reserva de cuarto

- POST : {{base_url}}/rooms/
- Valores para type : 
'SIM', 'Simple'
'DBL', 'Double'
'MAT', 'Matrimonial'
'SPL', 'Special'
- request:
 ```
curl --location 'http://localhost:8000/api/booking/make/' \
--header 'Content-Type: application/json' \
--data '{
  "room": 3,
  "guest": 7,
  "checkin_date": "2023-07-26",
  "checkout_date": "2023-07-30"
}'
 ```
response :
 ```
{
  "room": 3,
  "guest": 7,
  "checkin_date": "2023-07-26",
  "checkout_date": "2023-07-30"
}
 ```
4. Obtener detalles de una reserva
- GET : {{base_url}}/booking/{ID}/
- request :
 ```
curl --location 'http://localhost:8000/api/booking/25/'
 ```
- response:
 ```
{
    "id": 25,
    "uuid": "7e24310c-d60f-4b74-8818-2bd71f74ba88",
    "reservation_date": "2023-07-22T12:38:06.709106Z",
    "checkin_date": "2023-07-26",
    "checkout_date": "2023-07-30",
    "total_nights": 4,
    "guest": "hernan4 chambi4",
    "room": "Simple - Habitación simple con vis...",
    "status": "PAID"
}
 ```
5. Realizar un pago
- POST : {{base_url}}/invoices/process/
- Valores para  payment_method : 
'CREDIT_CARD', 'Tarjeta Credito'
'DEBIT_CARD', 'Tarjeta Debito'
'CASH', 'Efectivo'
'QR', 'QR'
- request:
 ```
curl --location 'http://localhost:8000/api/invoices/process/' \
--header 'Content-Type: application/json' \
--data '{
  "booking": 25,
  "payment_method": "CREDIT_CARD",
  "total": "454.26"
}'
 ```
response :
 ```
{
  "booking": 25,
  "payment_method": "CREDIT_CARD",
  "total": "454.26"
}
 ```
6. Obtener detalles de un pago
- GET : {{base_url}}/invoices/{ID}/
- Request :
 ```
curl --location 'http://localhost:8000/api/invoices/3/'
 ```
- Response :
 ```
{
    "id": 3,
    "customer": {
        "id": 1,
        "username": "john.doe update",
        "email": "john.doe@example.com2",
        "name": "John update",
        "last_name": "Doe",
        "nit": null,
        "password": "pbkdf2_sha256$600000$xBCxmQfuqdDrVClfE15K1P$WC4W6yYNKGy0/b8fBLIe034nffcJhbnNwwIpz17kBeA="
    },
    "booking": {
        "id": 23,
        "uuid": "83155dd1-7722-40a9-8c6f-4e1a50dae1b7",
        "reservation_date": "2023-07-21T03:10:23.268455Z",
        "checkin_date": "2023-07-26",
        "checkout_date": "2023-07-30",
        "guest": "John update Doe",
        "room": "Simple - Habitación simple con vis...",
        "price_per_night": 100.5,
        "total_nights": 4,
        "room_charge": 402.0,
        "taxes": 52.26,
        "total": 454.26,
        "status": "PAID"
    },
    "uuid": "kBpUAcs37uWtH2dc4MSCkH",
    "payment_method": "CREDIT_CARD",
    "taxes": "52.26",
    "room_fee": "402.00",
    "total": "454.26",
    "payment_date": "2023-07-21",
    "description": null
}
 ```
## IV. Documentacion
Para documentar los diferentes endpoint se uso Swagger el cual esta disponible en :

http://ec2-3-144-82-130.us-east-2.compute.amazonaws.com/swagger

## IV. Testing
Se realizo las pruebas unitarias a los endpoints mas importantes.
 ```
python manage.py test -v2
 ```
 ```
System check identified no issues (0 silenced).
test_booking_can_be_cancelled (apps.booking.tests.test_booking_cancellation.BookingCancellationTestCase) ... ok
test_booking_can_be_created (apps.booking.tests.test_booking_creation.BookingCreationTestCase) ... ok
test_booking_can_be_listed (apps.booking.tests.test_booking_listing.BookingListingTestCase) ... ok
test_booking_can_be_retrieved (apps.booking.tests.test_booking_retrieval.BookingRetrievalTestCase) ... ok
test_invoice_can_be_created (apps.invoice.tests.test_invoice_create.InvoiceCreationTestCase) ... ok
test_invoice_can_be_listed (apps.invoice.tests.test_invoice_listing.InvoiceListingTestCase) ... ok
test_invoice_can_be_retrieved (apps.invoice.tests.test_invoice_retrieval.InvoiceRetrievalTestCase) ... ok
test_room_can_be_created (apps.room.tests.test_room_create.RoomCreateTestCase) ... ok
test_room_can_be_deleted (apps.room.tests.test_room_delete.RoomDeleteTestCase) ... ok
test_room_can_be_listed (apps.room.tests.test_room_list.RoomListTestCase) ... ok
test_room_can_be_retrieved (apps.room.tests.test_room_retrieve.RoomRetrieveTestCase) ... ok
test_room_can_be_updated (apps.room.tests.test_room_update.RoomUpdateTestCase) ... ok
test_user_can_be_deleted (apps.user.tests.test_user_delete.UserDeleteTestCase) ... ok
test_user_list (apps.user.tests.test_user_list.UserListTestCase) ... ok
test_user_can_be_registered (apps.user.tests.test_user_registration.UserRegistrationTestCase) ... ok
test_user_can_be_retrieved (apps.user.tests.test_user_retrieval.UserRetrievalTestCase) ... ok
test_user_can_be_updated (apps.user.tests.test_user_update.UserUpdateTestCase) ... ok

----------------------------------------------------------------------
Ran 17 tests in 6.995s

OK
 ```
## IV. Cobertura de codigo
Se uso la herramienta coverage para medir la cobertura de las pruebas de la aplicacion.
```
coverage run manage.py test
coverage report
coverage html
```
```
Name                                                                              Stmts   Miss  Cover
-----------------------------------------------------------------------------------------------------
apps/__init__.py                                                                      0      0   100%
apps/base/__init__.py                                                                 0      0   100%
apps/base/admin.py                                                                    1      0   100%
apps/base/apps.py                                                                     4      0   100%
apps/base/migrations/__init__.py                                                      0      0   100%
apps/base/models.py                                                                  20      1    95%
apps/base/tests.py                                                                    1      0   100%
apps/booking/__init__.py                                                              0      0   100%
apps/booking/admin.py                                                                 1      0   100%
apps/booking/apps.py                                                                  4      0   100%
apps/booking/email_service.py                                                         5      3    40%
apps/booking/migrations/0001_initial.py                                               7      0   100%
apps/booking/migrations/0002_initial.py                                               7      0   100%
apps/booking/migrations/0003_alter_booking_options_and_more.py                        4      0   100%
apps/booking/migrations/__init__.py                                                   0      0   100%
apps/booking/models.py                                                               34      3    91%
apps/booking/routers.py                                                               5      0   100%
apps/booking/serializers.py                                                          64      8    88%
apps/booking/tests/__init__.py                                                        0      0   100%
apps/booking/tests/base.py                                                           12      0   100%
apps/booking/tests/booking_factory.py                                                15      0   100%
apps/booking/tests/test_booking_cancellation.py                                      12      0   100%
apps/booking/tests/test_booking_creation.py                                           9      0   100%
apps/booking/tests/test_booking_listing.py                                           10      0   100%
apps/booking/tests/test_booking_retrieval.py                                         10      0   100%
apps/booking/views.py                                                                42      7    83%
apps/invoice/__init__.py                                                              0      0   100%
apps/invoice/admin.py                                                                 1      0   100%
apps/invoice/apps.py                                                                  4      0   100%
apps/invoice/migrations/0001_initial.py                                               9      0   100%
apps/invoice/migrations/0002_alter_historicalinvoice_payment_method_and_more.py       4      0   100%
apps/invoice/migrations/__init__.py                                                   0      0   100%
apps/invoice/models.py                                                               24      0   100%
apps/invoice/routers.py                                                               5      0   100%
apps/invoice/serializers.py                                                          49      2    96%
apps/invoice/tests/__init__.py                                                        0      0   100%
apps/invoice/tests/base.py                                                           15      0   100%
apps/invoice/tests/invoce_factory.py                                                 16      0   100%
apps/invoice/tests/test_invoice_create.py                                            10      1    90%
apps/invoice/tests/test_invoice_listing.py                                           10      0   100%
apps/invoice/tests/test_invoice_retrieval.py                                          8      0   100%
apps/invoice/utils.py                                                                21      0   100%
apps/invoice/views.py                                                                34      3    91%
apps/room/__init__.py                                                                 0      0   100%
apps/room/admin.py                                                                    1      0   100%
apps/room/apps.py                                                                     4      0   100%
apps/room/migrations/0001_initial.py                                                  5      0   100%
apps/room/migrations/0002_room_photo.py                                               4      0   100%
apps/room/migrations/__init__.py                                                      0      0   100%
apps/room/models.py                                                                  19      0   100%
apps/room/routers.py                                                                  5      0   100%
apps/room/serializers.py                                                              6      0   100%
apps/room/tests/__init__.py                                                           0      0   100%
apps/room/tests/room_factory.py                                                      11      0   100%
apps/room/tests/test_room_create.py                                                  10      0   100%
apps/room/tests/test_room_delete.py                                                  11      0   100%
apps/room/tests/test_room_list.py                                                    11      0   100%
apps/room/tests/test_room_retrieve.py                                                11      0   100%
apps/room/tests/test_room_update.py                                                  13      0   100%
apps/room/views.py                                                                    6      0   100%
apps/user/__init__.py                                                                 0      0   100%
apps/user/admin.py                                                                    3      0   100%
apps/user/apps.py                                                                     4      0   100%
apps/user/migrations/0001_initial.py                                                  8      0   100%
apps/user/migrations/0002_historicaluser_nit_user_nit.py                              4      0   100%
apps/user/migrations/__init__.py                                                      0      0   100%
apps/user/models.py                                                                  32      6    81%
apps/user/routers.py                                                                  5      0   100%
apps/user/serializers.py                                                             32      4    88%
apps/user/tests/__init__.py                                                           0      0   100%
apps/user/tests/base.py                                                               7      0   100%
apps/user/tests/test_user_delete.py                                                  10      0   100%
apps/user/tests/test_user_list.py                                                    10      0   100%
apps/user/tests/test_user_password_set.py                                             9      4    56%
apps/user/tests/test_user_registration.py                                            11      0   100%
apps/user/tests/test_user_retrieval.py                                               10      0   100%
apps/user/tests/test_user_update.py                                                  11      0   100%
apps/user/tests/user_factory.py                                                      11      0   100%
apps/user/views.py                                                                   57     12    79%
hotel_v1/__init__.py                                                                  0      0   100%
hotel_v1/settings.py                                                                 32      0   100%
hotel_v1/urls.py                                                                      8      0   100%
manage.py                                                                            12      2    83%
-----------------------------------------------------------------------------------------------------
TOTAL                                                                               870     56    94%
```
El reporte generado esta en [htmlcov/index.html](htmlcov%2Findex.html)

## IV. Implementacion local
Build y ejecución del contenedor:  
    ```
    sudo docker build -t mydjangoapp .
    ```  
    ```
    sudo docker run -p 8000:8000 mydjangoapp
    ```

La API estará disponible en http://localhost:8000/

## V. Convenciones

Aquí puedes incluir algunas convenciones y mejores prácticas para el desarrollo y documentación de tu API, como:

- Uso de autenticación JWT para proteger las rutas sensibles.
- Seguir las convenciones de nombres para las rutas y nombres de recursos.
- Utilizar paginación para respuestas con muchos datos.
- Incluir ejemplos claros en la documentación para facilitar el uso de la API.
