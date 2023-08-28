from matplotlib import pyplot as plt

form = r"$\int\frac{x^5}{\sqrt[3]{1+x^3}} \mathrm{d}x = \frac{1}{3} \int \frac{x^3}{\sqrt[3]{1+x^3}} \mathrm{d}x^3 =$"
plt.text(0.01, 0.9, form, fontsize=15)
form = r"$= \frac{1}{3} \int \frac{x^3+1}{\sqrt[3]{1+x^3}} \mathrm{d}(1+x^3) - \frac{1}{3} \int \frac{1}{\sqrt[3]{1+x^3}} \mathrm{d}(1+x^3) =$"
plt.text(0.01, 0.7, form, fontsize=15)
form = r"$= \frac{1}{3} \int (x^3+1)^\frac{2}{3}\mathrm{d}(x^3+1) - \frac{1}{3} (1+x^3)^{-\frac{1}{3}} \mathrm{d}(x^3+1) =$"
plt.text(0.01, 0.5, form, fontsize=15)
form = r"$= \frac{1}{5}(1+x^3)^\frac{5}{3} - \frac{1}{2} (1+x^3)^\frac{2}{3} + C =$"
plt.text(0.01, 0.3, form, fontsize=15)
form = r"$= \sqrt[3]{(1+x^3)^2}(0,2x^3-0,3)+ C$"
plt.text(0.01, 0.1, form, fontsize=15)

fig = plt.gca()
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)

plt.show()

plt.text(0.01, 0.9, 'В данном примере мы во первых привели', fontsize=14)
plt.text(0.01, 0.8, 'dx^3 за счет этого вынесли 1/3 за интеграл.', fontsize=14)
plt.text(0.01, 0.7, 'Следующим шагом привели к 1+x^3.', fontsize=14)
plt.text(0.01, 0.6, 'Дальше инегрируем наше выражение.', fontsize=14)
plt.text(0.01, 0.5, 'Мысленно можем представить, что 1+x^3', fontsize=14)
plt.text(0.01, 0.4, 'это просто x или какое либо число.', fontsize=14)
plt.text(0.01, 0.3, 'В дальнейшем упрощаем, высчитываем и', fontsize=14)
plt.text(0.01, 0.2, 'получаем наш ответ:', fontsize=14)
form = r"$= \sqrt[3]{(1+x^3)^2}(0,2x^3-0,3)+ C$"
plt.text(0.01, 0.1, form, fontsize=15)

fig = plt.gca()
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)

plt.show()

form = r"$\int_1^{e^3} \sqrt[3]{x} ln_ x_ \mathrm{d}x = $"
plt.text(0.01, 0.9, form, fontsize=15)
form = r"$= \left| \genfrac {}{}{0}{}{u = lnx_ du = \frac{dx}{x}}{dv = x^\frac{1}{3}dx_ v = \frac{3}{4}x^\frac{4}{3}}\right| =$"
plt.text(0.01, 0.7, form, fontsize=15)
form = r"$ = \frac{3}{4}x^\frac{4}{3} lnx \int_1^{e^3}-\frac{3}{4}_  \int_1^{e^3} x^\frac{4}{3} \frac{dx}{x} = $"
plt.text(0.01, 0.5, form, fontsize=15)
form = r"$ = \frac{3}{4}(e^4lne^3-1^\frac{4}{3}ln1) - \frac{3}{4} \int_1^{e^3}x^\frac{1}{3}dx = $"
plt.text(0.01, 0.3, form, fontsize=15)
form = r"$ = \frac{9}{4} e^4 - \frac{9}{16} x^\frac{4}{3} \int_1^{e^3} = \frac{9}{4} e^4 - \frac{9}{16}(e^4-1) = \frac{27}{16} e^4 + \frac{9}{16}$"
plt.text(0.01, 0.1, form, fontsize=15)

fig = plt.gca()
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)

plt.show()

plt.text(0.01, 0.9, 'А в этом примере мы использовали способ', fontsize=14)
plt.text(0.01, 0.8, 'решения - интегрирование по частям.', fontsize=14)
plt.text(0.01, 0.7, 'Разделяем нашу функцию на части', fontsize=14)
plt.text(0.01, 0.6, 'и по частям высчитываем.', fontsize=14)
plt.text(0.01, 0.5, 'Затем полученное возвращаем в уравнение', fontsize=14)
plt.text(0.01, 0.4, 'и высчитываем.', fontsize=14)
plt.text(0.01, 0.3, 'В итоге получаем наш ответ:', fontsize=14)
form = r"$\frac{27}{16} e^4 + \frac{9}{16}$"
plt.text(0.01, 0.15, form, fontsize=15)

fig = plt.gca()
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)

plt.show()