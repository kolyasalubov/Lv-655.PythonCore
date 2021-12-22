import covid_statistics_requests as cs

permanent_notes = f"{cs.today}" """     last day confirmed        """ f"{cs.total_confirmed} \n "
others_countries_notes = f"{cs.today}  \n{cs.country}        |  population             |  {cs.population} \n                last day confirmed         {cs.total_confirmed} \n"

try:
    if cs.country == "Ukraine":
                
        with open("Projects\Anastasiia-web\Project_1\API_covid_statistics\src\statistics_Ukraine.txt", "a", encoding="utf-8") as ukr_st:
            ukr_st.write(permanent_notes)

    elif cs.country == "Poland":

        with open("Projects\Anastasiia-web\Project_1\API_covid_statistics\src\statistics_Poland.txt", "a", encoding="utf-8") as pol_st:
            pol_st.write(permanent_notes)

    else:

        with open("Projects\Anastasiia-web\Project_1\API_covid_statistics\src\statistics_others.txt", "a", encoding="utf-8") as oth_st:
            oth_st.write(others_countries_notes)
except Exception as ex:
    print(ex)


print(f"Population in {cs.country}: {cs.population}")
print(f"Last Day confirmed Covid-19 cases in {cs.country}: {cs.total_confirmed}")
print(f"Total confirmed Covid-19 cases in {cs.country}: {cs.total_confirmed_cases}")
print(f"Total death due to confirmed Covid-19 cases in {cs.country}: {cs.total_death}")
print(f"Your file is up-to-date")
