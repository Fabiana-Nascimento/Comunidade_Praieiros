from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from comunidadeimpressionadora.models import Usuario
from flask_login import current_user
class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField('Confirmação da Senha', validators=[DataRequired(), EqualTo('senha')])
    botao_submit_criarconta = SubmitField('Criar Conta')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('E-mail já cadastrado. Cadastre-se com outro e-mail ou faça login para continuar')


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    lembrar_dados = BooleanField('Lembrar Dados de Acesso')
    botao_submit_login = SubmitField('Fazer Login')


class FormEditarPerfil(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    foto_perfil = FileField('Atualizar foto de perfil', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif'])])
    curso_safadeza = BooleanField('Mestre da Safadeza')
    curso_dancarino = BooleanField('Dançarino Profissional')
    curso_finesse = BooleanField('Devoradora de Ossos')
    curso_chique = BooleanField('Chiquefina')
    curso_obra = BooleanField('Musa dos Pedreiros')
    curso_bisca = BooleanField('A Biscate da Turma')
    curso_coco = BooleanField('Coco Ninja')
    curso_sacola = BooleanField('Fashionista Rústico')
    curso_lata = BooleanField('Derrubador de Garrafas')
    curso_tanque = BooleanField('Gerente da Maquina de Lavar Roupa')
    curso_espanhol = BooleanField('Me / Yo - Poliglota')
    curso_fome = BooleanField('Fome Infinita')
    curso_marmita = BooleanField('Rei da Meia Marmita')
    curso_patrao = BooleanField('Mestre do Sofrimento Dietético')
    curso_ovo = BooleanField('OVOlucionária')
    curso_penosas = BooleanField('Comandante das Penosas')
    curso_gato = BooleanField('Gato Prendado')
    curso_canavial = BooleanField('Rei do Canavial')
    curso_java = BooleanField('Menino do Java')
    curso_viaja = BooleanField('Viaja na Maionese')
    curso_loca = BooleanField('Cai Cai da Estrela')



    botao_submit_editarperfil = SubmitField('Confirmar Edição')

    def validate_email(self, email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError('Já existe um usuário com cadastrado com este e-mail. Cadastre outro e-mail')

class FormCriarPost(FlaskForm):
    titulo = StringField('Titulo do Post', validators=[DataRequired(), Length(2,140)])
    corpo = TextAreaField('Escreva seu post aqui', validators=[DataRequired()])
    botao_submit = SubmitField('Criar Post')
