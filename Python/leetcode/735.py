from collections import deque


def asteroidCollision(asteroids):
    st = deque()
    for ast in asteroids:
        if ast > 0:
            st.append(ast)
        else:
            while st and abs(ast) > st[-1] and st[-1] > 0:
                st.pop()
            if st and abs(ast) == st[-1]:
                st.pop()
            elif not st or st[-1] < 0: st.append(ast)
    return list(st)
