import imageio
from pathlib import Path



# Create Gif and remove each .png file

image_path = Path('Game2048/temp')

images = list(image_path.glob('*.png'))
image_list = []
for file_name in images:
    image_list.append(imageio.imread(file_name))


# Cree le gif dans la racine du dossier
imageio.mimwrite('Game2048/Your_game2048.gif', image_list, fps=5)
