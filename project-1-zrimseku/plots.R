library(ggplot2)

data_activities <- read.csv(file='nr_categories.csv')

ggplot(data_activities, aes(sub_category, nr_activities)) + 
  geom_bar(fill="#459671", position = "dodge", stat="identity") + 
  facet_grid(. ~ category, scales = "free_x", space = "free_x") +
  labs(title="Number of activities per category", x="Sub category", y="Activities") +
  theme(axis.text.x=element_text(angle=90, vjust = 0.5, hjust=1), plot.title = element_text(hjust = 0.5)) +
  scale_y_continuous(expand = c(0,0), limits = c(0,50))



data_missing <- read.csv(file='nr_missing.csv')

ggplot(data_missing, aes(sub_category, nr_missing)) + 
  geom_bar(fill="#459671", position = "dodge", stat="identity") + 
  facet_grid(. ~ category, scales = "free_x", space = "free_x") +
  labs(title="Average number of missing elements", x="Sub category", y="Missing elements") +
  theme(axis.text.x=element_text(angle=90, vjust = 0.5, hjust=1), plot.title = element_text(hjust = 0.5)) +
  scale_y_continuous(expand = c(0,0), limits = c(0,5))

