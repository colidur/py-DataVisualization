#PieChart
import matplotlib.pyplot as plt


labels = 'Python', 'C++', 'Ruby', 'PHP', 'Java', 'Perl'
sizes = [33, 52, 12, 57, 62, 28]
separated = (.2, .05, .05, .05, .05, .05)

plt.pie(sizes, labels=labels, autopct='%1.1f%%', explode=separated)
plt.axis('equal')

plt.show()