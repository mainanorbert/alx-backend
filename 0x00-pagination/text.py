def paginate_dataset(dataset, page, page_size):
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return dataset[start_index:end_index]

# Example dataset
dataset = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Paginate the dataset
page = 2
page_size = 3
paginated_data = paginate_dataset(dataset, page, page_size)

print(paginated_data)

