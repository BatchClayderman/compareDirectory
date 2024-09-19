import os
from sys import exit
from time import sleep, time
EXIT_SUCCESS = 0
EXIT_FAILURE = 1
EOF = (-1)
PLATFORM = __import__("platform").system().upper()
CLEAR_SCREEN_COMMAND = ("CLS" if "WINDOWS" == PLATFORM else "clear") if __import__("sys").stdin.isatty() else None
ncols = 120


def compareFileContent(sourceFp:str, targetFp:str) -> bool:
	with open(sourceFp, "rb") as sf:
		with open(targetFp, "rb") as tf:
			a, b = sf.read(1), tf.read(1)
			while a and b:
				if a != b:
					return False
				a, b = sf.read(1), tf.read(1)
			return a == b # both should be empty at the same time if the two files are the same

def compare(sourceP:str, targetP:str, flag:bool = True) -> bool:
	sourcePath, targetPath, doesCompareFileContent = str(sourceP), str(targetP), bool(flag)
	sourceD, sourceF, targetD, targetF = [], [], [], []
	addingD, removalD, addingF, removalF, differenceF = [], [], [], [], []
	for root, dirs, files in os.walk(sourcePath):
		for directory in dirs:
			sourceD.append(os.path.relpath(os.path.join(root, directory), sourcePath))
		for f in files:
			sourceF.append(os.path.relpath(os.path.join(root, f), sourcePath))
	for root, dirs, files in os.walk(targetPath):
		for directory in dirs:
			targetD.append(os.path.relpath(os.path.join(root, directory), targetPath))
		for f in files:
			targetF.append(os.path.relpath(os.path.join(root, f), targetPath))
	print("len(sourceD) = {0}".format(len(sourceD)))
	print("len(sourceF) = {0}".format(len(sourceF)))
	print("len(targetD) = {0}".format(len(targetD)))
	print("len(targetF) = {0}".format(len(targetF)))
	for d in sourceD:
		if d in targetD:
			targetD.remove(d)
		else:
			removalD.append(d)
	for d in targetD:
		if d not in sourceD:
			addingD.append(d)
	for f in sourceF:
		if f in targetF:
			targetF.remove(f)
			if doesCompareFileContent and not compareFileContent(os.path.join(sourcePath, f), os.path.join(targetPath, f)):
				differenceF.append(f)
		else:
			removalF.append(f)
	for f in targetF:
		if f not in sourceF:
			addingF.append(f)
	print("addingD = {0}".format(addingD))
	print("removalD = {0}".format(removalD))
	print("addingF = {0}".format(addingF))
	print("removalF = {0}".format(removalF))
	if doesCompareFileContent:
		print("differenceF = {0}".format(differenceF))
		print("Totally {0} folders added, {1} folders removed, {2} files added, {3} files removed, and {4} different items. ".format(len(addingD), len(removalD), len(addingF), len(removalF), len(differenceF)))
	else:
		print("Totally {0} folders added, {1} folders removed, {2} files added, and {3} files removed. ".format(len(addingD), len(removalD), len(addingF), len(removalF)))
	return not any([addingD, removalD, addingF, removalF, differenceF])

def main() -> int:
	try:
		sourceDirectory = input("Please input the source directory: ").replace("\"", "")
		targetDirectory = input("Please input the folder directory: ").replace("\"", "")
		print("Start to compare. ")
		startTime = time()
		bRet = compare(sourceDirectory, targetDirectory)
		endTime = time()
		print("Finish comparing. ")
		print("The time used is {0:.3f} second(s). ".format(endTime - startTime))
		input()
		return EXIT_SUCCESS if bRet else EXIT_FAILURE
	except BaseException as e:
		print("Exceptions occurred. Details are as follows. \n{0}".format(e))
		input()
		return EOF



if __name__ == "__main__":
	exit(main())