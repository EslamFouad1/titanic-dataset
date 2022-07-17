def plot_count_dist(data, bin_df, label_column, target_column, figsize=(20, 5), use_bin,df):
    if use_bin_df:
        fig = plt.figure(figsize = figsize)
        plt.subplot(1, 2, 1)
        sns.countplot(y=target_column, data = bin_df);
        plt.subplot(1, 2, 2)
        sns.distplot(data.loc[data[label_column] == 1][target_column],
                    kde_kws={"label": "survived"});
        sns.distplot(data.loc[data[label_column] == 0][target_column],
                    kde_kws={"albel": "not survived"})
    else:
        fig = plt.figure(figsize=figsize)
        plt.subplot(1, 2, 1)
        sns.countplot(y=target_column, data = data);
        dplt.subplot(1, 2, 2)
        sns.distplot(data.loc[data[label_column] == 1][target_column],
                     kde_kws={"label":"Survived"})
        sns.distplot(data.loc[data[label_column]==0][target_column]
                     kde_kws={"label": "Did not survive"}),
