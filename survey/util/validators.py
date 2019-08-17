"""
Validators for numeric values go here
"""
from django.core.validators import MinValueValidator, MaxValueValidator


AGE_GROUP_VALIDATORS = [
    MaxValueValidator(150),
    MinValueValidator(0)
]

IS_NOT_NEGATIVE_VALIDATOR = [
    MinValueValidator(0)
]