# dati del problema
deposito_iniziale = 10000
tasso_interesse = 0.05

# inizializzazione delle variabili
deposito_corrente = deposito_iniziale
anno = 0

# ciclo while basato su un contatore
# Qual è il deposito dopo 10 anni?
while anno < 10:
    interesse_maturato = deposito_corrente * tasso_interesse
    deposito_corrente = deposito_corrente + interesse_maturato
    anno = anno + 1     # incremento del contatore

print(f"Dopo 10 anni il deposito è {deposito_corrente:.2f}")


# inizializzazione delle variabili
deposito_corrente = deposito_iniziale
anno = 0

# ciclo while basato su un evento
while deposito_corrente < 2 * deposito_iniziale:
    interesse_maturato = deposito_corrente * tasso_interesse
    deposito_corrente = deposito_corrente + interesse_maturato
    anno = anno + 1

print(f"Il deposito è raddoppiato dopo {anno} anni")