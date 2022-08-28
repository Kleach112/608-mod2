{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a60a6add-7067-437e-a171-d3c43d448bc9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n",
      "475\n",
      "79.16666666666667\n"
     ]
    }
   ],
   "source": [
    "values = (47, 95, 88, 73, 88, 84)\n",
    "Count = len(values)\n",
    "Total = sum(values)\n",
    "Mean = Total/Count\n",
    "\n",
    "print(Count)\n",
    "print(Total)\n",
    "print(Mean)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "73a016c4-35e6-4c91-afe7-7a11466f5d4b",
   "metadata": {},
   "outputs": [],
   "source": [
    "import statistics"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "6ef7f85b-de3a-4f5c-b77b-ae53dee77cd4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "88"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "statistics.mode(values)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "ec3e4223-8b4c-4bb1-a9a6-d03b04101887",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "86.0"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "statistics.median(values)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "c041d1a9-fd99-4d0d-bf4f-7c2bafe12670",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "79.16666666666667"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "statistics.mean(values)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "320fb145-0bf9-48f2-8248-a836bfec0d2d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Count: 5\n",
      "Total: 12868\n",
      "Mean: 2573.6\n",
      "Median: 2190\n",
      "Mode: 3271\n"
     ]
    }
   ],
   "source": [
    "#total number of discipline incidents by building for all high schools over the last 5 years - YTD\n",
    "HS_Incidents = (3271, 1972, 2164, 2190, 3271)\n",
    "Count = len(HS_Incidents)\n",
    "Total_Inc = sum(HS_Incidents)\n",
    "Mean = statistics.mean(HS_Incidents)\n",
    "Median = statistics.median(HS_Incidents)\n",
    "Mode = statistics.mode(HS_Incidents)\n",
    "\n",
    "print(f'Count: {Count}')\n",
    "print(f'Total: {Total_Inc}')\n",
    "print(f'Mean: {Mean}')\n",
    "print(f'Median: {Median}')\n",
    "print(f'Mode: {Mode}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3ae907ac-e557-43c0-85a4-7535c6a5e0c5",
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
