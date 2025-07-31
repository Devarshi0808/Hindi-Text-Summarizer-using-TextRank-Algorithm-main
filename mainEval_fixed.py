import os
from pathlib import Path

# Use relative paths that work on any OS
current_dir = Path(__file__).parent
ref_folder_location = current_dir / 'IO' / 'human_output'
machine_folder_location = current_dir / 'IO' / 'machine_output'

scoreList = []

# Create class to hold counters
class Score:
    def __init__(self, id):
        self.id = id
        self.pre = 0
        self.rec = 0
        self.f1 = 0
        self.match = 0

def buildList(fileN):
    """Build list of sentences from a file"""
    try:
        with open(fileN, 'r', encoding='utf-8') as filePointer:
            s = '$'
            for refSumLine in filePointer:
                refSumLine = refSumLine.strip()
                s = s + refSumLine
            s = s.strip('$')
            listVal = s.split(u'\u0964')
            return listVal
    except FileNotFoundError:
        print(f"Warning: File {fileN} not found")
        return []
    except Exception as e:
        print(f"Error reading file {fileN}: {e}")
        return []

def main():
    print("Hindi Text Summarizer Evaluation")
    print("=" * 40)
    
    # Check if directories exist
    if not ref_folder_location.exists():
        print(f"Error: Reference folder not found: {ref_folder_location}")
        return
    
    if not machine_folder_location.exists():
        print(f"Error: Machine output folder not found: {machine_folder_location}")
        return
    
    # Process files
    for i in range(1, 11):  # Process files 1-10
        machinFile = f'article{i}_system1.txt'
        refFile = f'article{i}_reference1.txt'
        machinFile = machine_folder_location / machinFile
        refFile = ref_folder_location / refFile
        
        # Check if both files exist
        if not machinFile.exists():
            print(f"Warning: Machine file not found: {machinFile}")
            continue
        if not refFile.exists():
            print(f"Warning: Reference file not found: {refFile}")
            continue
        
        # Open and process files
        refList = buildList(refFile)
        machineList = buildList(machinFile)
        
        if len(machineList) <= 0 or len(refList) <= 0:
            print(f"Warning: Empty files for article {i}")
            continue
        
        # Calculate metrics
        matchSet = set(refList) & set(machineList)
        matchCount = len(matchSet)
        
        # Create object
        o = Score(i)
        o.match = matchCount
        
        # Calculate precision and recall
        if len(machineList) > 0:
            o.pre = o.match / len(machineList)
        else:
            o.pre = 0
            
        if len(refList) > 0:
            o.rec = o.match / len(refList)
        else:
            o.rec = 0
        
        # Calculate F1 score
        if (o.pre + o.rec) > 0:
            o.f1 = 2 * ((o.pre * o.rec) / (o.pre + o.rec))
        else:
            o.f1 = 0
            
        scoreList.append(o)
    
    # Display results
    if scoreList:
        print("\nID  =>  F1 Score")
        print("-" * 20)
        s = 0
        for i in scoreList:
            s += i.f1
            strO = f"{i.id} => {i.f1:.4f}"
            print(strO)
        
        avgFScore = s / len(scoreList)
        print(f"\nTotal Avg. F1 Score => {avgFScore:.4f}")
    else:
        print("No valid files found for evaluation")

if __name__ == "__main__":
    main() 