from csv import DictReader
from sets.Block import Block
from sets.BlockList import BlockList
from sets.Coin import Coin

def block_load(csv_path: str) -> BlockList:
    """
    Load blocks from a CSV file into a BlockList.

    Args:
        csv_path (str): The path to the CSV file containing block data.

    Returns:
        BlockList: A BlockList object containing the loaded blocks.
    """
    block_list = BlockList()
    with open(csv_path, 'r') as csv_file:
        reader = DictReader(csv_file)
        for row in reader:
            block = Block(
                id=int(row['id']),
                energy=Coin(
                    mental=int(row['energia mental']),
                    physical=int(row['energia fisica'])
                )
            )
            block_list.append(block)
    return block_list