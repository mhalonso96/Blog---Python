from django.core.exceptions import ValidationError


def validade_png(image):
    if not image.name.lower().endswith('.png'):
        print('Não é uma imagem png')
        raise ValidationError(
                'Imagem precisa ser PNG'
        )