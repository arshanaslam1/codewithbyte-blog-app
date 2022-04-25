CodeWithByte-blog

A Django blog app with features of a standard blogging platform.

    General info
    Standalone Project
    Screenshots
    Features
    Technologies
    Setup

General info

An Open-Source Django blogging app like Medium and Real Python. It has features of a standard blogging platform.
Standalone Project
You can get it from its GitHub Repo.

Screenshots

Main Page
![Screenshot from 2022-04-23 00-16-39](https://user-images.githubusercontent.com/54641847/164784615-c861ab2c-94fa-4e72-9456-116e1a0cceb7.png)

Article Detail
![Screenshot from 2022-04-23 00-32-27](https://user-images.githubusercontent.com/54641847/164785374-2f58895a-98f9-4bdb-826e-04f3611015fd.png)

Catagory List
![Screenshot from 2022-04-23 00-28-23](https://user-images.githubusercontent.com/54641847/164784809-9c908aa8-3cf1-4c66-9d8c-44a2dcc807a7.png)

Tag List
![Screenshot from 2022-04-23 00-28-11](https://user-images.githubusercontent.com/54641847/164784835-8bcf0171-a382-4ddb-8073-ce725054217f.png)

Author List
![Screenshot from 2022-04-23 00-27-48](https://user-images.githubusercontent.com/54641847/164784864-ed18c39d-1aff-49dd-9580-b0dd190f922b.png)

Author Resume
![Screenshot from 2022-04-23 00-30-46](https://user-images.githubusercontent.com/54641847/164788161-74679ce0-51d5-4f56-abe3-562486cb3b4e.png)
![Screenshot from 2022-04-23 00-56-23](https://user-images.githubusercontent.com/54641847/164785161-34e29ea7-9dff-4ce8-968c-720516f10926.png)
![Screenshot from 2022-04-23 00-56-36](https://user-images.githubusercontent.com/54641847/164785174-805bcc71-a63c-4237-bbe5-7031b2bc6e6e.png)
![Screenshot from 2022-04-23 00-57-00](https://user-images.githubusercontent.com/54641847/164785194-aaddb140-0d4e-4f4d-8bac-a16ac158df94.png)

Author Resume Edit
![Screenshot from 2022-04-23 01-22-30](https://user-images.githubusercontent.com/54641847/164788462-ea1acb23-e0d9-4159-a2b5-37a7cd068de5.png)

Create Article
![Screenshot from 2022-04-23 00-31-29](https://user-images.githubusercontent.com/54641847/164785604-6be6b543-c261-4e1e-bbeb-6c32cc5449dd.png)


Features

    Mobile App Version
    WYSIWYG Editor
    Account Verification
    Author Login
    Author Password Reset
    Category List
    Category Articles List
    Tag List
    Tag Articles List
    Author List
    Author Articles List
    Related Articles
    Comments
    Likes
    Articles Search
    Article Social Media Share
    Article Number of Views
    Auhtor Resume/ Profile
    Responsive on all devices
    Pagination
    Admin can Add Tagss and Catagories
    Clean Code

Technologies

    Python 3.9
    Jquery
    Ajax
    Django 4.0
    HTML5
    CSS3
    Bootstrap 4
    Summernote
    MySQL
    SQLite
    PostgreSQL

Setup

To run this app, you will need to follow these 3 steps:
1. Requirements

    a Laptop

    Text Editor or IDE (eg. vscode, PyCharm)

    Python 3.8 +

    Django 4.0 +

2. Install Python and Pipenv

    Python3

    Pipenv

3. Local Setup and Running on Windows, Linux and Mac OS
4. Change Data Base Setting 
    If use AWS RDS set value True and AWS Credential and for SQL Lite Set False

  ```
      
USE_AWS_RDS = True
if USE_AWS_RDS:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ.get('DATABASE_NAME'),
            'USER': os.environ.get('DATABASE_USER'),
            'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
            'HOST': os.environ.get('DATABASE_HOST'),
            'PORT': os.environ.get('DATABASE_PORT'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

   
  ```             

5. Change Media and Static File Setting if use local server then set False 
and if you want to use AWS S3 Then set Value True and cofigure Credential


  ```
      
# S3
USE_S3 = True
if USE_S3:
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
    AWS_QUERYSTRING_AUTH = False
    AWS_S3_FILE_OVERWRITE = True
    AWS_DEFAULT_ACL = None

    STATICFILES_LOCATION = 'static'
    STATICFILES_STORAGE = 'Online_Portfolio_and_Blog_With_CMS.aws.utils.StaticStorage'
    STATIC_URL = 'https://{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)

    MEDIAFILES_LOCATION = 'media'
    DEFAULT_FILE_STORAGE = 'Online_Portfolio_and_Blog_With_CMS.aws.utils.MediaStorage'
    MEDIA_URL = 'htts://{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
else:
    STATIC_URL = 'static/'
    # Location of static files
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    # Base url to serve media files
    MEDIA_URL = '/media/'
    # Path where media is stored
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

   
  ```     


 6. Email Settings (Production)
    
      ```
      
    EMAIL_BACKEND = ''
    EMAIL_HOST = ''
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ""
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True

   
  ``` 
