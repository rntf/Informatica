##
#  Questo programma calcola una stima di pi greco simulando 
#  lanci di freccette su un bersaglio quadrato.
#

import random

TRIES = 10000

hits = 0
for i in range(TRIES):

    # Genera due numeri casuali compresi tra –1 e 1.
    r = random.random()
    x = -1 + 2 * r
    r = random.random()
    y = -1 + 2 * r

    # Oppure:
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)

    # Verifica se il punto appartiene al cerchio unitario.
    if x * x + y * y <= 1:
        hits = hits + 1

# Il rapporto hits / tries è circa uguale al rapporto 
# area del cerchio / area del quadrato = pi / 4.

pi_estimate = 4.0 * hits / TRIES
print("Estimate for pi:", pi_estimate)
