import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def read_data_from_file(file_name):
    with open(file_name, 'r') as file:
        data = [int(line.strip()) for line in file]
    return data

def selection_sort_with_animation(arr):
    n = len(arr)
    fig, ax = plt.subplots()
    start_time = time.time()
    
    def update_plot(frame):
        ax.clear()
        if frame >= n:
            return
        min_index = frame
        for j in range(frame + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[frame], arr[min_index] = arr[min_index], arr[frame]
        ax.scatter(range(len(arr)), arr)
        
        # Exibe o tempo decorrido
        elapsed_time = time.time() - start_time
        ax.text(0.02, 0.95, f"Tempo: {elapsed_time:.4f} segundos", transform=ax.transAxes)

    ani = animation.FuncAnimation(fig, update_plot, frames=range(n + 1), repeat=False)
    plt.show()

# Exemplo de uso
file_name = "lista_gerada4.txt"
data = read_data_from_file(file_name)
selection_sort_with_animation(data)
