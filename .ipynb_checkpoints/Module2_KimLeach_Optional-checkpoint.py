{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4434ec6f-0f57-452a-946b-990847f22ff6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[36, 27, 30, 21, 19, 35, 33, 23, 29, 27, 19, 24, 33, 16, 15, 22, 32, 36, 26, 15, 21, 25, 19, 25, 28, 21, 22, 17, 32, 34, 34, 36, 31, 26, 22, 36, 20, 18, 29, 31, 30, 29, 31, 16, 28, 23, 17, 23, 31, 19, 32, 23, 16, 35, 35, 22, 34, 27, 32, 34, 34, 32, 35, 30, 22, 25, 26, 27, 17, 17, 18, 15, 28, 32, 28, 22, 25, 20, 18, 21, 17, 28, 17, 36, 20, 23, 22, 33, 25, 21, 24, 31, 36, 25, 22, 21, 18, 30, 24, 24, 30]\n"
     ]
    }
   ],
   "source": [
    "# Create a list of random numbers in a reasonable ACT Score range to simulate test scores\n",
    "import random\n",
    "randomlist = []\n",
    "for i in range(0,101):\n",
    "    n = random.randint(15,36)\n",
    "    randomlist.append(n)\n",
    "print(randomlist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "49d0e3b7-7d1c-4f66-9452-826f5e1052a7",
   "metadata": {},
   "outputs": [],
   "source": [
    "import statistics"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "fe02c0d0-7a34-4a9a-9377-de9eae12c025",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of ACT Tests Taken: 101\n",
      "Sum of ACT Scores: 2601\n",
      "Average ACT Score: 25.75\n",
      "Median ACT SCore: 25\n",
      "Most Frequent ACT Score: 22\n",
      "Building Grade is C\n"
     ]
    }
   ],
   "source": [
    "# find the count, sum, mean, median, and mode of random test scores generated\n",
    "\n",
    "ACT_Scores = (36, 27, 30, 21, 19, 35, 33, 23, 29, 27, 19, 24, 33, 16, 15, 22, 32, 36, 26, 15, 21, 25, 19, 25, 28, 21, 22, 17, 32, 34, 34, 36, 31, 26, 22, 36, 20, 18, 29, 31, 30, 29, 31, 16, 28, 23, 17, 23, 31, 19, 32, 23, 16, 35, 35, 22, 34, 27, 32, 34, 34, 32, 35, 30, 22, 25, 26, 27, 17, 17, 18, 15, 28, 32, 28, 22, 25, 20, 18, 21, 17, 28, 17, 36, 20, 23, 22, 33, 25, 21, 24, 31, 36, 25, 22, 21, 18, 30, 24, 24, 30)\n",
    "\n",
    "Count = len(ACT_Scores)\n",
    "Total = sum(ACT_Scores)\n",
    "Mean = statistics.mean(ACT_Scores)\n",
    "Median = statistics.median(ACT_Scores)\n",
    "Mode = statistics.mode(ACT_Scores)\n",
    "\n",
    "print(f'Number of ACT Tests Taken: {Count}')\n",
    "print(f'Sum of ACT Scores: {Total}')\n",
    "print(f'Average ACT Score: {Mean:.2f}')\n",
    "print(f'Median ACT SCore: {Median}')\n",
    "print(f'Most Frequent ACT Score: {Mode}')\n",
    "\n",
    "if Mean >= 32:\n",
    "    print ('Building Grade is A')\n",
    "elif Mean >=28:\n",
    "    print ('Building Grade is B')\n",
    "elif Mean >=24:\n",
    "    print ('Building Grade is C')\n",
    "elif Mean >=20:\n",
    "    print ('Building Grade is D')\n",
    "else:\n",
    "    print ('Building Grade is F')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c093aa00-18c9-4aa5-9d20-9908e8b1a805",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
