from crg.ext.db.models import Especie, Genero, Local

def filterEspecie(q, args):
    especie = args.get('especie') if 'especie' in args else None
    if especie:
        q = q.join(Especie).filter(Especie.nome == especie)
        return q
    return q

def filterGenero(q, args):
    genero = args.get('genero') if 'genero' in args else None
    if genero:
        q = q.join(Especie).join(Genero).filter(Genero.nome == genero)
        return q
    return q

def filterLocal(q, args):
    local = args.get('local') if 'local' in args else None
    if local:
        q = q.join(Local).filter(Local.nome.like("%"+local+"%"))
        return q
    return q