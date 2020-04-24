"""
Django settings for message project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_^mf3_qdyn+-y)jr2mpb5h@#x*4*uaco-l1eo8f+efp*xykrze'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.messageForm.apps.MessageformConfig',
    'apps.tips.apps.TipsConfig',
    'apps.blog.apps.BlogConfig',
    'apps.universe.apps.UniverseConfig',
    'crispy_forms',
    'xadmin.apps.XAdminConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'message.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'message.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
#


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# 创建日志的路径
LOG_PATH = os.path.join(BASE_DIR, 'log')
# 如果地址不存在，则自动创建log文件夹
if not os.path.join(LOG_PATH):
    os.mkdir(LOG_PATH)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,#此选项开启表示禁用部分日志，不建议设置为True
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'#日志格式
        },
        'standard': {
            'format': '[%(asctime)s] [%(levelname)s] %(message)s'
        },
    },
    # 'filters': {
    #     'require_debug_true': {
    #         '()': 'django.utils.log.RequireDebugTrue',#过滤器，只有当setting的DEBUG = True时生效
    #     },
    # },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            # 'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
            'stream': 'ext://sys.stdout',

        },
        'file': {#重点配置部分
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': LOG_PATH+'/message.log',#日志保存文件
            'formatter': 'verbose',
            
        },
        'default': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            
            'filename': LOG_PATH+'/default.log',     #日志输出文件
            'maxBytes': 1024*1024*5,                  #文件大小
            'backupCount': 5,                         #备份份数
            'formatter':'standard',                   #使用哪种formatters日志格式
        },
        'warning': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            
            'filename': LOG_PATH+'/warning.log',
            'maxBytes': 1024*1024*5,                  #文件大小
            'backupCount': 5,
            'formatter': 'verbose'
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 1024*1024*5,                  #文件大小
            'backupCount': 5,
            'filename': LOG_PATH+'/error.log',
            'formatter': 'verbose'
        },
        'critical': {
            'level': 'CRITICAL',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 1024*1024*5,                  #文件大小
            'backupCount': 5,
            'filename': LOG_PATH+'/critical.log',
            'formatter': 'verbose'
        },
        'request_handler': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': LOG_PATH+'/script.log',
            'maxBytes': 1024*1024*5,
            'backupCount': 5,
            'formatter':'standard',
        },
        'scprits_handler': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename':LOG_PATH+'/script.log',
            'maxBytes': 1024*1024*5,
            'backupCount': 5,
            'formatter':'standard',
        }
    },
    'loggers': {
        'formLogin': {
            'handlers': ['request_handler', 'file'],
            'level': 'DEBUG',
            'filemode': 'a',
            'propagate': True,
        },
        'tipsLogin': {
            'handlers': ['request_handler', 'file'],
            'level': 'DEBUG',
            'filemode': 'a',
            'propagate': True,
        },
        'universeLogin': {
            'handlers': ['request_handler', 'file'],
            'level': 'DEBUG',
            'filemode': 'a',
            'propagate': True,
        },
        'info': {
            'handlers': ['default'],
            'level': 'INFO',
            'filemode': 'a',
            'propagate': True,
        },
        'warning': {
            'handlers': ['warning'],
            'level': 'WARNING',
            'filemode': 'a',
            'propagate': True,
        },
        'error': {
            'handlers': ['error'],
            'level': 'ERROR',
            'filemode': 'a',
            'propagate': True,
        },
        'critical': {
            'handlers': ['critical'],
            'level': 'CRITICAL',
            'filemode': 'a',
            'propagate': True,
        },
    },
}