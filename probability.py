# probability

# idea didn't work
# no good results


p = 1
knee = 5  # ratio at which probability is 99%
const = np.log(100) / knee


# probability
for i in range(6):
    if colors[i] != "ba" and colors[i] != "w":
        for j in range(i):
            if colors[j] != "ba" and colors[j] != "w":
                small_disti = 9999999
                small_distj = 9999999
                ai1 = 0
                ai2 = 0
                aj1 = 0
                aj2 = 0
                dist_out = 500
                dist_mid = 500
                for k in range(6):
                    for l in range(9):
                        if tilecol[k][l] == colors[i] and distances[k][l][
                            j] < small_disti:
                            small_disti = distances[k][l][j]
                            ai1 = k
                            ai2 = l
                        elif tilecol[k][l] == colors[j] and \
                                distances[k][l][
                                    i] < small_distj:
                            small_distj = distances[k][l][i]
                            aj1 = k
                            aj2 = l
                dist_out = abs(avgcol[ai1][ai2][0] - avgcol[aj1][aj2][0])
                if dist_out > 113:
                    dist_out = 256 - dist_out
                dist_mid = abs(avgcol[i][8][0] - avgcol[j][8][0])
                if dist_mid > 113:
                    dist_mid = 256 - dist_mid
                ratio = dist_out / dist_mid
                prob = 1 / (1 + mt.e ** (-(const * ratio)))
                p *= prob


print(p)