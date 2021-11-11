
from flask.helpers import url_for
from app import db
from flask_login import UserMixin, current_user
from datetime import datetime as dt
from werkzeug.security import generate_password_hash, check_password_hash
from app import login
from flask import flash



class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    email = db.Column(db.String(200), unique=True)
    password = db.Column(db.String(200))
    created_on =db.Column(db.DateTime, default=dt.utcnow)
    pokemon = db.relationship('Pokemon', backref='author', lazy='dynamic')
    wins = db.Column(db.Integer, default=0)
    losses = db.Column(db.Integer, default=0)

    def caught(self, poki):
        return poki in self.pokemon
    
    def catch(self, poki):
        if self.pokemon.query.filter_by(User.id).count() > 5:
            return flash(f'You can only catch 5 Pokemons', 'warning')
        else:
            self.pokemon.append(poki)
            db.session.commit

    def poki_attack(self, user2):
        total_user_attack = 0
        total_user_points =0 
        total_user_defense = 0
        for poki in current_user.pokemon:
            total_user_attack += int(poki.attack)
            total_user_points += int(poki.hp)
            total_user_defense += int(poki.defense)
        total_user2_attack = 0
        total_user2_points =0 
        total_user2_defense = 0
        for poki in user2.pokemon:
            total_user2_attack += int(poki.attack)
            total_user2_points += int(poki.hp)
            total_user2_defense += int(poki.defense) 
        if total_user2_attack > total_user_attack and total_user2_defense < total_user_defense:
            self.losses += 1
            user2.wins +=1
            self.save()
            user2.save()
            return False
            
        else:
            self.wins += 1
            user2.losses +=1
            self.save()
            user2.save()
            return True
                  

    def poki_points(self, user):
        pass

            

    def __reper__(self):
        return f'<User: {self.id} | {self.email}>'
    
    def from_dict(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = self.hash_password(data['password'])
    
    def hash_password(self, original_password):
        return generate_password_hash(original_password)
    
    def check_password_hash(self, login_password):
        return check_password_hash(self.password, login_password)

    def save(self):
        db.session.add(self)
        db.session.commit() 

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=dt.utcnow)
    date_updated = db.Column(db.DateTime, onupdate=dt.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    Name = db.Column(db.String(100))
    abilities = db.Column(db.String(100))
    base_experience = db.Column(db.String(100))
    sprite = db.Column(db.String(100))
    hp = db.Column(db.String(100))
    attack = db.Column(db.String(100))
    defense = db.Column(db.String(100))



    def from_dict(self, data):
        self.Name = data['Name']
        self.abilities = data['abilities']
        self.base_experience = data['base_experience']
        self.sprite = data['sprite']
        self.hp = data['hp']
        self.attack = data['attack']
        self.defense = data['defense']
        self.user_id = current_user.id

  
    
   

            
    
    # def uncatch(self,user):
    #     if self.is_caught(user):
    #         self.Name.remove(user)
    #         db.session.commit()

    
    def save(self):
        db.session.add(self) 
        db.session.commit() 

    def edit(self, new_name, new_abilities):
        self.name=new_name
        self.abilities=new_abilities
        self.save()
    
    def __repr__(self):
        return f'<id:{self.id} | Pokemon: {self.Name[:15]}>'