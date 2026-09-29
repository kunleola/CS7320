# HOWTO Work on Assignments

We will provide you with a Colab link to the assignment notebook.

Your submitted assignment notebook needs to be a complete project report with

- documentation (including your design choices), 
- code (with comments for sections that are difficult to understand), and
- results (e.g., tables with simulation results) with a short discussion of what they mean. 

Use the provided notebook cells and insert additional code and markdown cells as needed.

You have several options for working on the notebook. **Making a local copy breaks the relative links in the assignment.** Use the original assignment to find the correct paths.

## Option 1: Colab

You can work directly in Colab by using `File > Save a copy to Drive` (you will need a Google account). To use data files in Colab, go to the My Drive - Colab Notebooks folder in [Google Drive](https://drive.google.com) and copy the needed files there. Then mount Google Drive in your notebook and change to the notebook folder. Add the following code to a code cell:

```{python}
from google.colab import drive
import os

drive.mount('/content/drive')
os.chdir('/content/drive/My Drive/Colab Notebooks/')
```

You can execute shell commands. The following line lists the contents of the current directory. It should show the `.ipynb` files you have there.

```{python}
%ls
```

To create an HTML document from your rendered notebook, add a code cell with the following command to your Jupyter notebook. Run it after your document is completely rendered.
```{python}
%jupyter nbconvert --to html nameofyournotebook.ipynb
```

You can now download the created HTML file from your Google Drive.

## Option 2: Work Locally (e.g., VS Code)

You can download individual assignment notebooks using `File>Download>Download .ipynb` and then work locally on the project. You will need to download additional files as well.

Make sure that you have a copy of your assignment in a safe place with a backup (e.g., Google Drive).
If you want to use version control, create a new **private** repository and commit your code there.
